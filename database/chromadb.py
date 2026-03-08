import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    persist_directory="./memory",
    anonymized_telemetry=False
))

collection = client.get_or_create_collection(name="nova_memory")


def save_memory(text):
    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )


def get_memory(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    if results["documents"]:
        return "\n".join(results["documents"][0])

    return ""