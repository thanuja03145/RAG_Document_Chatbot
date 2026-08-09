from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents_into_chunks(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    
    chunks = []
    for doc in documents:
        split_texts = text_splitter.split_text(doc["content"])
        for chunk in split_texts:
            chunks.append({
                "text": chunk,
                "source": doc["filename"]
            })
            
    return chunks
