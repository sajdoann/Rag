from rag.loader import load_all_texts
from rag.splitter import split_text
from rag.embedder import embed_and_store
from rag.retriever import retrieve_similar
from rag.generator import generate_answer

def build_db(data_dir):
    raw_sources = load_all_texts(data_dir)
    print(f"Found {len(raw_sources)} documents in {data_dir}")
    print("Document sources:")
    for src_name, _ in raw_sources:
        print("-", src_name)

    chunks = []
    for source_name, text in raw_sources:
        split_docs = split_text(text)
        for doc in split_docs:
            doc.metadata["source"] = source_name
        chunks.extend(split_docs)
    embed_and_store(chunks)

def query_rag_system(question):
    docs, metadatas = retrieve_similar(question)
    print("Docs:")
    for doc,meta in zip(docs,metadatas):
        print(doc)
        print(meta)
        print('-' * 20)

    answer = generate_answer(question, docs)
    return answer, metadatas