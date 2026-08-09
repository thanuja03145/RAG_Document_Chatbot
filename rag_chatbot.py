import os
import re

class StandaloneRAGChain:
    def __init__(self, retriever, api_key=None):
        self.retriever = retriever

    def _extract_relevant_sentences(self, query, context, max_sentences=4):
        # Clean page markers and line breaks
        cleaned_context = re.sub(r'--- Page \d+ ---', '', context)
        sentences = [s.strip() for slen in cleaned_context.split('\n') for s in slen.split('. ') if len(s.strip()) > 10]
        
        query_words = set(re.findall(r'\w+', query.lower())) - {'what', 'is', 'the', 'are', 'a', 'an', 'in', 'of', 'for', 'to', 'this', 'give', 'me', 'tell'}
        
        scored_sentences = []
        for s in sentences:
            s_words = set(re.findall(r'\w+', s.lower()))
            score = len(query_words.intersection(s_words))
            scored_sentences.append((score, s))
            
        scored_sentences.sort(key=lambda x: x[0], reverse=True)
        
        # Pick top unique sentences
        selected = []
        seen = set()
        for score, s in scored_sentences:
            if s not in seen:
                selected.append(s)
                seen.add(s)
            if len(selected) >= max_sentences:
                break
                
        return selected if selected else sentences[:max_sentences]

    def __call__(self, inputs):
        query = inputs.get("query", "").strip()
        docs = self.retriever.invoke(query)
        
        if not docs:
            return {
                "result": "No relevant information found in the uploaded document.",
                "source_documents": []
            }

        context_text = "\n".join([doc.page_content for doc in docs])
        relevant_info = self._extract_relevant_sentences(query, context_text)

        # Build clean dynamic response
        formatted_bullets = "\n".join([f"• {sentence}" for sentence in relevant_info])
        
        result_text = f"### 💡 Answer for: *\"{query}\"*\n\n{formatted_bullets}"

        return {
            "result": result_text,
            "source_documents": docs
        }

def setup_rag_chain(vector_db, api_key=None):
    retriever = vector_db.as_retriever(search_kwargs={"k": 4})
    return StandaloneRAGChain(retriever, api_key=api_key)
