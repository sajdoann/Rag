from rag.loader import load_all_texts
from rag.splitter import split_text
from rag.embedder import embed_and_store
from rag.retriever import retrieve_similar
from rag.generator import generate_answer

def build_db(data_dir):
    raw_texts = load_all_texts(data_dir)
    chunks = []
    for text in raw_texts:
        chunks.extend(split_text(text))
    embed_and_store(chunks)

def query_rag_system(question):
    docs = retrieve_similar(question)
    answer = generate_answer(question, docs)
    return answer