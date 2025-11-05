🧠 Local Retrieval-Augmented Text Generation (RAG)

A fully offline Retrieval-Augmented Generation (RAG) system that combines semantic search with transformer-based text generation.
This project demonstrates how to build a local, API-free pipeline for knowledge-grounded responses using Python, PyTorch, Hugging Face Transformers, Sentence-Transformers, and FAISS.

🚀 Overview

Large Language Models (LLMs) are powerful but often rely on cloud APIs or lack grounding in local data.
This project solves that by creating a local RAG pipeline that retrieves relevant text chunks from a custom dataset and generates context-aware answers — all running offline.

Core idea:

Retrieve relevant information from a local knowledge base → Use a lightweight local model (TinyLlama / Phi-2) → Generate grounded responses.

🧩 Features

🧠 Semantic Search: Retrieve relevant chunks using embeddings from Sentence-Transformers.

🔍 Vector Indexing: Store and query embeddings efficiently with FAISS.

🤖 Local Generation: Use open LLMs (TinyLlama or Phi-2) via Hugging Face Transformers for text generation.

⚙️ Offline Execution: No external APIs required — everything runs locally.

🧱 Modular Architecture: Separated components for embedding, retrieval, and generation.

🗂️ Project Structure
├── main.py             # Orchestrates the pipeline
├── embedder.py         # Generates and indexes embeddings
├── retriever.py        # Retrieves top-k relevant text chunks
├── generator.py        # Loads the local model for text generation
├── data.txt            # Knowledge base / reference text
└── README.md           # Project documentation

⚙️ Installation

Clone the repository

git clone https://github.com/JoshDilipkumarPatel/Local-RAG-System.git
cd Local-RAG-System


Create a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install torch transformers sentence-transformers faiss-cpu

💡 Usage

Prepare your data
Place your text data inside data.txt.
Example:

Blockchain is a decentralized ledger technology that ensures transparency and security in digital transactions.


Run the app

python main.py


Ask questions interactively

Enter your question: What is blockchain?


Get grounded, context-aware answers directly from your local knowledge base.

🧠 Example Output
Enter your question: What is blockchain?

Answer:
Blockchain is a decentralized ledger system that records transactions securely across a distributed network, ensuring transparency and trust without intermediaries.

🔬 Tech Stack

Language Model: TinyLlama / Phi-2 (Hugging Face Transformers)

Embeddings: Sentence-Transformers (MiniLM)

Vector Search: FAISS

Framework: PyTorch

Language: Python

📈 Key Learnings

Implemented semantic retrieval and vector search using FAISS.

Integrated open-source LLMs for offline, context-driven generation.

Designed a reproducible, modular pipeline for future scalability and dataset extension.

📚 Future Improvements

Add UI interface (Streamlit or Gradio)

Integrate hybrid retrieval (BM25 + dense embeddings)

Evaluate with STS and retrieval metrics (Recall@k, MRR)

Extend to multi-document summarization
