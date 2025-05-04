# Rag 🦞

This system implements a Retrieval-Augmented Generation (RAG) pipeline 
for processing and querying data (in my case .pdf of lecture slides and transcripts .txt in `data/`). It allows users to build a database of materials and ask questions, retrieving relevant information from the database.


## Code overview
```aiignore
rag/
├── loader.py      # Loads .pdf and .txt files from a directory
├── splitter.py    # Splits long texts into overlapping chunks
├── embedder.py    # Embeds text chunks and stores them in ChromaDB
├── retriever.py   # Retrieves top-k similar chunks for a query
├── generator.py   # Uses an LLM to generate answers from context
├── pipeline.py    # High-level build/query functions
main.py            # CLI entry point for building DB or asking questions
llm_interface.py   # Unified interface for multiple LLM backends
config.py          # Configuration file for LLM provider and model
```
### rag/ stack Notes
- **Loader** uses PyMuPDF for PDF and standard file reading for text files.
- **Splitter** uses LangChain’s RecursiveCharacterTextSplitter for chunking.
- **Embeddings** use all-MiniLM-L6-v2 for fast & accurate performance.
- **Retriever** uses ChromaDB for efficient similarity search. Retrieves top-k chunks based on cosine similarity.
- **Generator** uses LLM (specified by `config.py`) to generate answers based on retrieved context.
- **Pipeline** orchestrates the entire process from loading to answering.

## Requirements
### Python venv
- Python3 3.12.3 (or higher) - chromadb did not like lower
- create virtual environment (once): `python3 -m venv ~/virtualenvs/rag_env` (choose your path)
- source the virtual environment (every time you want to run): `source ~/virtualenvs/rag_env/bin/activate`
- `pip install -r requirements.txt`
- All setup! :)
 
### LLM Provider
- **[Ollama](https://github.com/ollama/ollama)**: Install Ollama and set up the model you want to use.
  - `curl -fsSL https://ollama.com/install.sh | sh`
  - ``ollama pull <model_name>`` (e.g., `deepseek-r1:1.5b` (small ideal for cpu), `llama2`, `llama2-7b`, etc.)
  - `ollama run <model_name>` just to test the model
  - `./ollama serve` to run the model as a server

- you can implement other LLM providers by creating a new class in `llm_interface.py` and modifying the `config.py` file to use it.

## Usage
0. **Set up the environment**: Make sure you have the required Python version and packages installed. Activate your virtual environment.
    
        source ~/virtualenvs/rag_env/bin/activate
1. **Set up the LLM provider**: Choose provider in `config.py`. Make sure the model is downloaded and running.
    
    For Ollama:
    
    ```    
    ollama serve
    ```
1. **Build the database**:

    Run `python main.py build` to load and process files in the `data/` directory.
2. **Ask questions**:

    Run `python main.py --query "your question here"` to get answers based on the database.

### About transcript generation
- downloaded lectures with `download_lectures.sh`
- run whisper on [metacetrum](https://docs.metacentrum.cz/en/docs/computing/run-basic-job) to generate transcripts with `run_whisper.pbs`
- Unfortunatley metacentrum has memory limits I was hitting for some reason, so I transcribed around 4 lectures at a time. I used cpu only to jobs as I did not have to wait in queue for them that long.
4 transcriptions were usually done in 1-3 hours.

### Improvement ideas:
- idea extract timestamp of slide changes (botttom left corner number) 
    - why? connect transcripts and slides (possibly improve the transcription, combine transcription and slides)
- Metadata filtering
Allow filtering by document source or lecture topic (based on metadata in Document objects).
- GUI like https://www.chatpdf.com/ 
- apply to other domains (e.g., legal, medical, etc.)

