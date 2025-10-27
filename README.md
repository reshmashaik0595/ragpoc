# AIML - Generative AI - RAG POC

## Description

**RAG POC** is a Proof of Concept that integrates **Retrieval-Augmented Generation (RAG)** with a **Large Language Model (LLM)** to enhance information retrieval and response generation. This project combines the power of Mistral LLM with components like Ollama, ChromaDB, and a Streamlit frontend for interactive exploration.

## Technologies Used

- **Python** – Core programming language
- **Streamlit** – Web UI framework for building interactive apps
- **Ollama** – Framework to run and manage LLMs locally
- **Mistral** – Open-weight language model used in the backend
- **ChromaDB** – Vector database for semantic search and retrieval

## Installation

To set up and run the project, use the following commands:

```bash
# Clone the repository
git clone <repository-url>
cd rag-poc

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run LLM Provider
ollama serve

# Run Ollama Model
ollama run mistral

# Run the Streamlit app
streamlit run app.py

# Run the application
http://localhost:8501/

```

## ChromaDB Commands

```bash

python chroma_cli.py list               # List documents with embeddings (default: 10)

python chroma_cli.py list_docs <count>  # List only documents (default: 10)

python chroma_cli.py delete <_id>       # Delete docs by IDs

python chroma_cli.py delete             # Delete all


  # List all collection names

```

## Reference Links

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)
- [Mistral](https://mistral.ai/news/announcing-mistral-7b/)
- [ChromaDB](https://www.trychroma.com/)


