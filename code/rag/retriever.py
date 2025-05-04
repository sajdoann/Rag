import chromadb

def retrieve_similar(query, top_k=5, db_path="./embeddings/chroma", collection_name="lecture_docs"):
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_collection(name=collection_name)
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0], results.get("metadatas", [])[0]
