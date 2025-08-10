import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the FAISS index
INDEX_PATH = "vectorstore/faiss_index"
index = faiss.read_index(os.path.join(INDEX_PATH, "index.faiss"))

# Load metadata and chunks
with open(os.path.join(INDEX_PATH, "chunks.pkl"), "rb") as f:
    chunks = pickle.load(f)

with open(os.path.join(INDEX_PATH, "metadata.pkl"), "rb") as f:
    metadata = pickle.load(f)

def answer_query(query, k=5):
    """
    Takes a natural language question and returns the top-k matching chunks and their metadata.
    """
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = []
    for i in indices[0]:
        results.append((chunks[i], metadata[i]))

    return results