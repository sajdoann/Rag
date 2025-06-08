import chromadb
from sentence_transformers import SentenceTransformer
from typing import List

def embed_and_store(
    docs: List[object],
    db_path: str = "./embeddings/chroma",
    collection_name: str = "lecture_docs"
) -> None:
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_or_create_collection(name=collection_name)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [doc.page_content for doc in docs]
    embeddings = model.encode(texts, show_progress_bar=True)

    for i, (doc, emb) in enumerate(zip(docs, embeddings)):
        metadata = doc.metadata.copy()
        collection.add(
            documents=[doc.page_content],
            ids=[str(i)],
            embeddings=[emb.tolist()],
            metadatas=[metadata]
        )
