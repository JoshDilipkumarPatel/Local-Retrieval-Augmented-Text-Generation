import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

class Retriever:
    def __init__(self, embedder=None):
        self.embedder = embedder or SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.docs = None

    def build_index(self, docs):
        texts = [d.strip() for d in docs if d.strip()]
        embeddings = np.array(self.embedder.encode(texts, convert_to_numpy=True)).astype("float32")
        self.index = NearestNeighbors(n_neighbors=3, metric="cosine")
        self.index.fit(embeddings)
        self.docs = texts

    def retrieve(self, query, top_k=3):
        query_vec = np.array(self.embedder.encode([query], convert_to_numpy=True)).astype("float32")
        distances, indices = self.index.kneighbors(query_vec, n_neighbors=top_k)
        results = [self.docs[i] for i in indices[0]]
        return results
