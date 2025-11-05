🧠 Local Retrieval-Augmented Text Generation (RAG)

This project implements a fully local Retrieval-Augmented Generation (RAG) pipeline that combines semantic search with transformer-based text generation. It retrieves relevant information from a local knowledge base and generates context-aware responses — all running offline, without using any external APIs.

📖 Project Overview

Large Language Models (LLMs) are powerful but often ungrounded and dependent on cloud APIs.
This project demonstrates how to build a self-contained RAG system that can understand queries, retrieve relevant context, and generate grounded text responses — entirely on your local machine.

Here’s what happens inside:

Your text data is stored in data.txt and split into chunks.

Each chunk is converted into numerical embeddings using Sentence-Transformers (MiniLM).

The FAISS index stores these embeddings for fast semantic retrieval.

When a user asks a question, the most relevant chunks are retrieved.

A local language model (TinyLlama or Phi-2) generates a response using that context.

This setup creates a lightweight, modular, and completely offline text-generation system suitable for research, demos, and educational projects.

🚀 Features

End-to-end RAG pipeline: local data → embeddings → retrieval → context-based generation

Semantic similarity search: powered by Sentence-Transformers and FAISS

Offline language generation: runs locally via TinyLlama or Phi-2

Modular architecture: separate components for embedding, retrieval, and generation

Reproducible and scalable: easy to extend for larger datasets or other models

🛠️ Technologies Used

Python 3.x

PyTorch

Hugging Face Transformers

Sentence-Transformers

FAISS (Facebook AI Similarity Search)

📂 Project Structure
|── README.md              # Project documentation
├── main.py                # Orchestrates the full RAG pipeline
├── embedder.py            # Generates and indexes document embeddings
├── retriever.py           # Retrieves top relevant chunks for a query
├── generator.py           # Loads the local LLM and generates text
└── data.txt               # Knowledge base / reference text

⚡ Getting Started
1. Clone the repository
git clone https://github.com/JoshDilipkumarPatel/Local-RAG-System.git
cd Local-RAG-System

2. Install dependencies
pip install torch transformers sentence-transformers faiss-cpu

3. Add your data and run

Add your custom text to data.txt. Example:

Artificial Intelligence enables systems to learn from data and improve over time.


Then run:

python main.py

4. Interact

Ask questions interactively:

Enter your question: What is Artificial Intelligence?

💬 Example Output
Enter your question: What is Artificial Intelligence?

Answer:
Artificial Intelligence refers to computer systems that can perform tasks requiring human-like intelligence, such as learning, reasoning, and language understanding.

📊 Example Architecture Flow
data.txt → embeddings → FAISS index → retriever → generator (LLM) → response

✨ Future Improvements

Add UI with Streamlit or Gradio for interactive use

Introduce hybrid retrieval (BM25 + dense embeddings)

Evaluate using retrieval metrics (Recall@k, MRR)

Expand dataset for domain-specific knowledge bases
