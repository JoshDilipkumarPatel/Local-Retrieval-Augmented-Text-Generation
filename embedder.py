from sentence_transformers import SentenceTransformer

def get_embedder():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model
