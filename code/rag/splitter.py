from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def split_text(text, chunk_size=512, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)
    docs = []
    for i, chunk in enumerate(chunks):
        start_index = i * (chunk_size - chunk_overlap)
        docs.append(Document(page_content=chunk, metadata={"start_index": start_index}))
    return docs