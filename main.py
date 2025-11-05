from embedder import get_embedder
from retriever import Retriever
from generator import LocalGenerator

def load_knowledge(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text.split(". ")

def main():
    docs = load_knowledge("data/data.txt")
    embedder = get_embedder()
    retriever = Retriever(embedder)
    retriever.build_index(docs)
    generator = LocalGenerator()  # updated here

    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == "exit":
            break
        context = " ".join(retriever.retrieve(query))
        answer = generator.generate(context, query)
        print("\nAnswer:", answer)

if __name__ == "__main__":
    main()
