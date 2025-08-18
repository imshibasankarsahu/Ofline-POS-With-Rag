# rag_module.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd
#Loading the Inventory
def load_inventory(csv_path="inventory.csv"):
    df = pd.read_csv(csv_path)
    return df
# Embedding the Inventory Items
def embed_inventory(df, embedder_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(embedder_name)
    embeddings = model.encode(df['name'].tolist())
    return embeddings, model
#Building the FAISS Index
def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index
#Searching the Inventory (RAG Step)
def search_inventory(query, model, index, df, top_k=3):
    emb = model.encode([query])
    D, I = index.search(np.array(emb), top_k)
    return df.iloc[I[0]]
