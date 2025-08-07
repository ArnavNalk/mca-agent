from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np

def chunk_texts_with_tables(texts, tables):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_chunks = []
    metadata = []

    table_map = {t['filename']: t['tables'] for t in tables}

    for doc in texts:
        text = doc['text']
        filename = doc['filename']
        if filename in table_map:
            text += "\n\nTABLES:\n" + table_map[filename]

        chunks = splitter.split_text(text)
        all_chunks.extend(chunks)
        metadata.extend([filename] * len(chunks))

    return all_chunks, metadata

def embed_chunks(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings