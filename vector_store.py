from langchain_community.vectorstores import FAISS

def build_vector_store(text_chunks, embedding_model):
    texts = [chunk["text"] for chunk in text_chunks]
    metadatas = [{"source": chunk["source"]} for chunk in text_chunks]
    
    vector_db = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )
    return vector_db
