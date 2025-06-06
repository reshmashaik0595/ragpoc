from embedding_utils import chunk
from chroma_utils import insert_chunks

def ingest_text(text: str, source: str = "manual_input") -> int:
    chunks = chunk(text)
    insert_chunks(chunks, source)
    return len(chunks)
