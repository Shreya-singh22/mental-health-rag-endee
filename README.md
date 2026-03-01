# 🧠 RAG-Based Mental Health Assistant

A fully local Retrieval-Augmented Generation (RAG) system that provides grounded, context-aware mental health guidance using semantic search and a vector database.

Built with:
- 🧠 Sentence Transformers (MiniLM)
- ⚡ Endee (High-performance vector database)
- 🤖 Local LLM (Flan-T5)
- 🐳 Dockerized backend

---

## 🚀 Project Overview

This project implements a complete Retrieval-Augmented Generation (RAG) pipeline for a Mental Health Assistant.

The system:

1. Converts mental health knowledge into embeddings
2. Stores them in a vector database (Endee)
3. Retrieves relevant context using semantic similarity
4. Generates grounded responses using a local language model

Unlike simple chatbots, this system ensures responses are grounded in verified context instead of hallucinated outputs.

---

## 🏗️ Architecture
User Query
↓
Embedding (MiniLM)
↓
Vector Search (Endee)
↓
Top-K Relevant Chunks
↓
Local LLM (Flan-T5)
↓
Grounded Response


---

## 🧩 Tech Stack

| Component | Technology |
|------------|------------|
| Embeddings | SentenceTransformers (all-MiniLM-L6-v2) |
| Vector Database | Endee |
| LLM | Google Flan-T5 (local) |
| Backend | Python |
| Containerization | Docker |
| Similarity Metric | Cosine Similarity |
| Precision | float32 |

---

## 📂 Project Structure

mental-health-rag-endee/
│
├── src/
│ ├── ingest.py # Embedding + vector ingestion
│ ├── rag.py # Retrieval + Generation pipeline
│ ├── test_search.py # Semantic search testing
│ ├── test_rag.py # Full RAG testing
│ └── utils.py # Text chunking utility
│
├── data/
│ └── anxiety.txt
│
├── endee-server/
│ └── docker-compose.yml
│
├── .gitignore
└── README.md

---

