import faiss
import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "vector.index")
CHUNKS_PATH = os.path.join(BASE_DIR, "chunks.pkl")

class Retriever:
    def __init__(self):
        print("Loading index...")
        self.index = faiss.read_index(INDEX_PATH)

        print("Loading chunks metadata...")
        with open(CHUNKS_PATH, "rb") as f:
            self.chunks = pickle.load(f)

        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Prepare TF-IDF
        print("Building TF-IDF matrix...")
        self.texts = [chunk["text"] for chunk in self.chunks]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.texts)

    def retrieve(self, query, top_k=5):
        # ----- Semantic Search -----
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, semantic_indices = self.index.search(query_embedding, top_k)

        semantic_results = set(semantic_indices[0])

        # ----- Keyword Search -----
        query_tfidf = self.vectorizer.transform([query])
        keyword_scores = (self.tfidf_matrix @ query_tfidf.T).toarray().ravel()

        keyword_indices = np.argsort(keyword_scores)[-top_k:]

        keyword_results = set(keyword_indices)

        # ----- Combine Results -----
        combined_indices = list(semantic_results.union(keyword_results))

        results = [self.chunks[i] for i in combined_indices]

        return results
