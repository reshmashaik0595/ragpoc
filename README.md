# 🚀 AIML - Generative AI - Retrieval-Augmented Generation (RAG) POC

## 📌 Overview

This **Proof of Concept (POC)** demonstrates **Retrieval-Augmented Generation (RAG)** using a local **Large Language Model (LLM)** for enhanced information retrieval and intelligent responses. The system integrates **Mistral LLM** with **Ollama**, **ChromaDB**, and a **Streamlit** user interface to enable interactive exploration of knowledge bases.

## 🧠 Key Technologies

| Technology  | Purpose |
|-------------|---------|
| **Python**  | Core programming language |
| **Streamlit** | Interactive web UI framework |
| **Ollama**  | Local LLM runtime and management |
| **Mistral** | Open-weight language model powering generation |
| **ChromaDB** | Vector database for semantic search and document retrieval |

## ⚙️ Installation & Setup

Follow the steps below to install and run the RAG POC:

```bash
# Clone the repository
git clone <repository-url>
cd rag-poc

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 🔧 Configure Environment Variables

Create a `.env` file in the project root with the following values:

```env
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHROMA_DB_PATH=./chroma_db
OLLAMA_URL=http://127.0.0.1:11434/api/generate
OLLAMA_MODEL=mistral
```

### ▶️ Run the Application

```bash
# Start Ollama service
ollama serve

# Run the Mistral model
ollama run mistral

# Launch Streamlit app
streamlit run app.py
```

Open your browser and navigate to:

```
http://localhost:8501/
```

## 🗂️ ChromaDB CLI Commands

```bash
python chroma_cli.py list               # List documents with embeddings (default: 10)
python chroma_cli.py list_docs <count>  # List only document names (default: 10)
python chroma_cli.py delete <_id>       # Delete documents by ID
python chroma_cli.py delete             # Delete all documents
```

## 🔗 Reference Links

- **Python**: https://www.python.org/
- **Streamlit**: https://streamlit.io/
- **Ollama**: https://ollama.com/
- **Mistral LLM**: https://mistral.ai/news/announcing-mistral-7b/
- **ChromaDB**: https://www.trychroma.com/

## ✅ Summary

This POC delivers a local and efficient RAG pipeline using open-source technologies, enabling high-performance knowledge retrieval integrated with intelligent LLM-based response generation.

> 💡 Ideal for experimentation, enterprise prototyping, and AI solution development using local resources.
