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
    │
    ▼
FastAPI Backend (/ask)
    │
    ▼
SentenceTransformer (MiniLM)
    │
    ▼
Query Embedding (384-d vector)
    │
    ▼
Endee Vector Database (Cosine Similarity Search)
    │
    ▼
Top-K Relevant Context Retrieved
    │
    ▼
Prompt Construction
    │
    ▼
Local LLM (Flan-T5)
    │
    ▼
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

```
mental-health-rag-endee/
│
├── src/
│   ├── ingest.py          # Embedding + vector ingestion
│   ├── rag.py             # Retrieval + generation pipeline
│   ├── test_search.py     # Semantic search testing
│   ├── test_rag.py        # Full RAG testing
│   └── utils.py           # Text chunking utility
│
├── data/
│   └── anxiety.txt        # Knowledge base file
│
├── endee-server/
│   └── docker-compose.yml # Vector DB server setup
│
├── .gitignore
└── README.md
```

---

## 🗄️ How Endee is Used in This Project

This project uses **Endee** as the vector database service for storing and retrieving embeddings.

Endee runs as a Docker-based server and handles:

- Storing document embeddings
- Performing similarity search
- Managing vector collections
- Serving retrieval requests for the RAG pipeline

---

## ⚙️ Why Endee?

Endee is used because:

- ✅ It supports fast vector similarity search
- ✅ It integrates easily with Python
- ✅ It runs locally via Docker
- ✅ It scales for larger embedding datasets
- ✅ It separates storage from application logic

This makes the RAG system modular and production-ready.

---

## 🔄 How It Works in This Project

### 1️⃣ Endee Server Starts

The vector database is started using:

```bash
cd endee-server
docker-compose up
```

This launches the Endee container and exposes the vector database service.

---

### 2️⃣ Data Ingestion (`ingest.py`)

When you run:

```bash
python src/ingest.py
```

The following happens:

1. The `anxiety.txt` file is loaded.
2. The text is split into smaller chunks.
3. Each chunk is converted into an embedding using an embedding model.
4. The embeddings are stored inside an Endee collection.

At this point, Endee now contains vector representations of your knowledge base.

---

### 3️⃣ Semantic Search (`test_search.py`)

When a query is given:

- The query is converted into an embedding.
- Endee performs similarity search.
- The most relevant chunks are returned.

This allows the system to retrieve contextually similar mental health content.

---

### 4️⃣ RAG Pipeline (`rag.py`)

In the full RAG workflow:

1. User asks a question.
2. Query embedding is generated.
3. Endee retrieves relevant document chunks.
4. Retrieved chunks are passed to the LLM.
5. The LLM generates a grounded, context-aware response.

Endee ensures that responses are based on real stored knowledge rather than pure model memory.

---

## 🛡️ Importance in Mental Health Applications

Using Endee ensures:

- Reduced hallucination
- Evidence-based responses
- Context-grounded answers
- Scalable knowledge storage

This is especially important for mental health applications where reliability matters.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mental-health-rag-endee.git
cd mental-health-rag-endee
```

### 2️⃣ Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Start Endee Vector Database
```bash
cd endee-server
docker compose up -d
```

### 4️⃣ Ingest data
```bash
cd ../src
python ingest.py
```

### 5️⃣ Test Semantic Search
```bash
python test_search.py
```

### 6️⃣ Run Full RAG Pipeline
```bash
python test_rag.py
```
### Expected Output
```bash
🧠 Local RAG Response:

Deep breathing exercises can help manage anxiety naturally...
```



