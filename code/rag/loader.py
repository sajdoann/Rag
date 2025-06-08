import os
import pymupdf as fitz
from pathlib import Path
from typing import Iterator

def load_pdf_text(pdf_path: Path) -> str:
    doc = fitz.open(str(pdf_path))
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return text

def load_txt(file_path: Path) -> str:
    with file_path.open( 'r', encoding='utf-8') as f:
        return f.read()

def load_all_texts(data_dir: Path) -> Iterator[tuple[str, str]]:
    for file in data_dir.glob("**/*"):
        if file.suffix == ".pdf":
            yield (str(file), load_pdf_text(file))
        elif file.suffix == ".txt":
            yield (str(file), load_txt(file))
