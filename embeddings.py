from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model(api_key=None):
    # Free, local embedding model that doesn't need API requests or close connections
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
