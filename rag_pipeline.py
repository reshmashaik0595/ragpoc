from chroma_utils import find_similar
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def query_ollama(prompt: str, model: str = None) -> str:
    if model is None:
        model = os.getenv("OLLAMA_MODEL")

    ollama_url = os.getenv("OLLAMA_URL")
    if not ollama_url:
        raise ValueError("OLLAMA_URL is not set in environment variables.")

    response = requests.post(
        ollama_url,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    return response.json().get("response", "")


def rag_answer(question: str) -> str:
    docs = find_similar(question)
    context = "\n".join([doc for doc in docs if doc is not None])

    if context:
        prompt = (
            f"Use the following context to answer the question:\n\n"
            f"{context}\n\nQ: {question}\nA:"
        )
    else:
        prompt = (
            f"Answer the question based on your general knowledge, "
            f"but note that no specific context is available:\n\n"
            f"Q: {question}\nA:"
        )

    return query_ollama(prompt)
