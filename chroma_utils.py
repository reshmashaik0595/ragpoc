import uuid
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from dotenv import load_dotenv
import os
load_dotenv()

chroma_client = chromadb.PersistentClient(path=os.getenv("CHROMA_DB_PATH"))
embedding_fn = SentenceTransformerEmbeddingFunction(model_name=os.getenv("EMBEDDING_MODEL"))

collection = chroma_client.get_or_create_collection(
    name="documents",
    embedding_function=embedding_fn
)


def insert_chunks(chunks, source="manual_input"):
    metadatas = [{"source": source, "text": chunk} for chunk in chunks]
    documents = chunks
    ids = [str(uuid.uuid4()) for _ in chunks]
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    return {
        "metadatas": metadatas,
        "documents": documents,
        "ids": ids,
    }


def find_similar(query_text, top_k=5):
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )

    docs = results['documents'][0]
    return docs
