import os
#import fitz  # PyMuPDF
from pathlib import Path

# def load_pdf_text(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = "\n".join(page.get_text() for page in doc)
#     doc.close()
#     return text

def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_all_texts(data_dir):
    texts = []
    for file in Path(data_dir).glob("**/*"):
        if file.suffix == ".pdf":
            # raise error, no pdf supported
            print("NOP PDF SUPPORT YET:)")
            #texts.append(load_pdf_text(file))
        elif file.suffix == ".txt":
            texts.append(load_txt(file))
    return texts
