import os
import faiss
import numpy as np
import pickle

from preprocessing.extract_text import extract_all_texts
from preprocessing.extract_tables import extract_all_tables
from preprocessing.chunk_and_embed import chunk_texts_with_tables, embed_chunks

# 1. Load and extract
texts = extract_all_texts("data/reports/")
tables = extract_all_tables("data/reports/")

# 2. Chunk + embed
chunks, metadata = chunk_texts_with_tables(texts, tables)
embeddings = embed_chunks(chunks)

# 3. Save index and metadata
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

os.makedirs("vectorstore/faiss_index", exist_ok=True)
faiss.write_index(index, "vectorstore/faiss_index/index.faiss")

with open("vectorstore/faiss_index/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

with open("vectorstore/faiss_index/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("✅ Vector store created and saved.")