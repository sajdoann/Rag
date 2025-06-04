import chromadb
from pathlib import Path

def retrieve_similar(query: str, top_k: int = 5,
                     db_path: Path = Path("./embeddings/chroma"),
                     collection_name: str = "lecture_docs") -> tuple[list[str], dict]:
    chroma_client = chromadb.PersistentClient(path=str(db_path))
    collection = chroma_client.get_collection(name=collection_name)
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0], results.get("metadatas", [])[0]
