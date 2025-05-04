# 🦞 Rag

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline for querying lecture materials (PDF slides and `.txt` transcripts) using local computation only.

Users can build a searchable vector database from lecture content and ask natural-language questions to receive answers grounded in the relevant documents.

Example outputs located in: `example-outputs/`. They were geenrated with Ollama's `deepseek-r1:1.5b` model as is in `config.py`.

---

## 📁 Code Overview

```
rag/
├── loader.py        # Loads .pdf and .txt files from a directory
├── splitter.py      # Splits long texts into overlapping chunks
├── embedder.py      # Embeds text chunks and stores them in ChromaDB
├── retriever.py     # Retrieves top-k similar chunks for a query
├── generator.py     # Uses an LLM to generate answers from context
├── pipeline.py      # High-level build/query functions
main.py              # CLI entry point for building DB or asking questions
llm_interface.py     # Unified interface for multiple LLM backends
config.py            # Configuration for LLM provider and model
```

### Component Notes

- **Loader**: Uses PyMuPDF for PDFs and standard file reading for text files.
- **Splitter**: Uses LangChain’s `RecursiveCharacterTextSplitter` for robust chunking.
- **Embedder**: Utilizes `all-MiniLM-L6-v2` for fast, high-quality text embeddings.
- **Retriever**: Queries ChromaDB for top-k similar chunks using cosine similarity.
- **Generator**: Leverages an LLM (as defined in `config.py`) to answer questions from retrieved context.
- **Pipeline**: Orchestrates all steps: load → split → embed → retrieve → generate.

---

## ⚙️ Requirements

### 🐍 Python Virtual Environment

> Requires Python **3.12.3** or higher (older versions cause issues with ChromaDB).

```bash
# Create virtual environment (one-time)
python3 -m venv ~/virtualenvs/rag_env

# Activate environment (every time)
source ~/virtualenvs/rag_env/bin/activate

# Install dependencies (one time)
pip install -r requirements.txt
```

---

### 🧠 LLM Provider

#### Recommended: [Ollama](https://github.com/ollama/ollama)

1. **Install Ollama**  
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Download a model**  
   ```bash
   ollama pull deepseek-r1:1.5b
   # or try: ollama pull llama2, llama2-7b, etc.
   ```

3. **Run the model server**  
   ```bash
   ollama serve
   ```

> Want to add another LLM backend?  
> Just create a new class in `llm_interface.py` and update `config.py` accordingly.

---

## 🚀 Usage

### 0. Activate Environment

```bash
source ~/virtualenvs/rag_env/bin/activate
```

### 1. Start the LLM Server

For Ollama:

```bash
ollama serve
```

### 2. Build the Vector Database

This loads and processes files from the `data/` directory:

```bash
python main.py build
```

### 3. Ask Questions

```bash
python main.py --query "What is the chain rule in backpropagation?"
```

---

## 📜 Transcript Generation

I generated transcripts from lecture videos:

1. Download `.mp4` videos using `download_lectures.sh`.
2. Run [Whisper](https://github.com/openai/whisper) on [MetaCentrum](https://docs.metacentrum.cz/en/docs/computing/run-basic-job) via `run_whisper.pbs`.

I typically run 3–4 videos at a time, each taking ~20 minutes to transcribe.

---

## ⚠️ Limitations

- Works great on CPU-only machines, but **LLM generation is slow** (~1 minute per answer).
- On machines with a GPU, generation drops to just a few seconds.
- **Retrieval is fast** (1–2 seconds) even without a GPU — showcasing the efficiency of the vector search!

> For real-time performance, I'd need better hardware or a cloud solution — but this system is intentionally designed for **fully local use**. ✅

---

## 💡 Improvement Ideas

- Extract slide change timestamps from the PDF (e.g. slides templated look at bottom-left page numbers change in video) to sync with transcripts.
- Add **metadata filtering** (e.g., by lecture title, source).
- Build a GUI like [chatpdf.com](https://www.chatpdf.com/).
- Apply RAG to other domains: legal, medical, etc.
- test if it would pass Milan Starka's publicly available questions for subjects:)
---

## 📚 Sources & Inspiration

- [Retrieval-Augmented Generation (RAG) summary paper (arXiv)](https://arxiv.org/pdf/2312.10997)
- [LangChain + ChromaDB RAG Tutorial (YouTube)](https://www.youtube.com/watch?v=tcqEUSNCn8I&ab_channel=pixegami)
