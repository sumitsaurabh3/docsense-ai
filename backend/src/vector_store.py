import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer
from src.loader import load_documents
from src.chunker import chunk_text


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "vector.index")
CHUNKS_PATH = os.path.join(BASE_DIR, "chunks.pkl")

def build_vector_store():
    print("Loading documents...")
    docs = load_documents()

    print("Chunking documents...")
    chunks = chunk_text(docs)

    texts = [chunk["text"] for chunk in chunks]

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Generating embeddings...")
    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    print("Saving index and metadata...")
    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("✅ Vector store built successfully!")

if __name__ == "__main__":
    build_vector_store()
