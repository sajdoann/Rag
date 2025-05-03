import chromadb
from sentence_transformers import SentenceTransformer

def embed_and_store(docs, db_path="./embeddings/chroma", collection_name="lecture_docs"):
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_or_create_collection(name=collection_name)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(docs, show_progress_bar=True)

    for i, (doc, emb) in enumerate(zip(docs, embeddings)):
        collection.add(documents=[doc], ids=[str(i)], embeddings=[emb.tolist()])