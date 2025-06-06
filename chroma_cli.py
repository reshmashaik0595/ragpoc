import sys
import os
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from dotenv import load_dotenv
from tabulate import tabulate
import textwrap
load_dotenv()

chroma_client = chromadb.PersistentClient(path=os.getenv("CHROMA_DB_PATH"))

embedding_fn = SentenceTransformerEmbeddingFunction(
    model_name=os.getenv("EMBEDDING_MODEL")
)

collection = chroma_client.get_or_create_collection(
    name="documents",
    embedding_function=embedding_fn
)

def format_full_embedding(vec):
    return "[" + ", ".join(f"{x:.4f}" for x in vec) + "]"

def wrap_text(text, width=70):
    if not isinstance(text, str):
        text = str(text)
    return "\n".join(textwrap.wrap(text, width=width))

def list_chunks_with_vectors(limit=10):
    try:
        results = collection.get(limit=limit, include=["embeddings", "documents", "metadatas"])
        documents = results.get("documents", [])
        metadatas = results.get("metadatas", [])
        ids = results.get("ids", [])
        embeddings = results.get("embeddings", [])

        if not documents:
            print(f"No documents found in collection '{collection.name}'")
            return

        rows = []
        for i in range(len(documents)):
            rows.append([
                str(ids[i]),
                wrap_text(metadatas[i], width=40),
                wrap_text(documents[i], width=50),
                wrap_text(format_full_embedding(embeddings[i]), width=70)
            ])

        print(tabulate(rows, headers=["ID", "Metadata", "Document", "Embedding"], tablefmt="fancy_grid"))

    except Exception as e:
        print("Error:", e)

def list_documents(limit=10):
    try:
        results = collection.get(limit=limit, include=["documents"])
        documents = results.get("documents", [])
        if not documents:
            print(f"No documents found in collection '{collection.name}'")
            return
        for i, doc in enumerate(documents, 1):
            print(f"{i}. {doc}\n")
    except Exception as e:
        print("Error:", e)

def delete_documents(ids=None):
    try:
        if ids:
            collection.delete(ids=ids)
            print(f"Deleted documents with IDs: {ids}")
        else:
            all_docs = collection.get()
            all_ids = all_docs["ids"]
            if all_ids:
                collection.delete(ids=all_ids)
                print(f"Deleted ALL documents from collection '{collection.name}'")
            else:
                print(f"No documents found in collection '{collection.name}'")
    except Exception as e:
        print("Error during deletion:", e)

def initialize_collection():
    print(f"Collection '{collection.name}' is ready (or already exists).")

def list_collections():
    collections = chroma_client.list_collections()
    if not collections:
        print("No collections found.")
    else:
        print("Available collections:")
        for c in collections:
            print(f"- {c.name}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python chroma_cli.py <command> [args]")
        print("Commands:")
        print("  list [limit]         - List documents with embeddings (default: 10)")
        print("  list_docs [limit]    - List only documents (default: 10)")
        print("  delete [id1 id2 ...] - Delete docs by IDs; omit IDs to delete all")
        print("  init                 - Initialize collection")
        print("  list_collections     - List all collection names")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        list_chunks_with_vectors(limit)
    elif command == "list_docs":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        list_documents(limit)
    elif command == "delete":
        ids = sys.argv[2:] if len(sys.argv) > 2 else None
        delete_documents(ids)
    elif command == "init":
        initialize_collection()
    elif command == "list_collections":
        list_collections()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
