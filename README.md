🧠 Mental Health RAG Assistant using Endee
📌 Project Overview

This project implements a domain-specific AI assistant for mental health guidance using Retrieval-Augmented Generation (RAG) and Endee as the vector database.

The system is designed to provide grounded, context-aware responses instead of generic or hallucinated outputs from standalone language models. By combining semantic search with controlled knowledge retrieval, the assistant ensures responses are based strictly on curated mental health content.

🎯 Problem Statement

Online mental health advice often suffers from:

Generic, non-personalized answers

Unsafe or misleading information

Lack of context grounding

Hallucinated outputs from LLMs

This project addresses these issues by:

Storing trusted mental health content in a vector database.

Retrieving relevant context using semantic similarity search.

Generating responses strictly grounded in retrieved information.

The result is a safer, domain-focused AI assistant.

🏗️ System Architecture

The system follows a standard RAG pipeline:

1️⃣ Data Ingestion

Mental health text files are chunked into smaller segments.

Each chunk is converted into embeddings using SentenceTransformers.

Embeddings are stored in Endee.

2️⃣ Vector Storage (Endee)

Endee is used as the persistent vector database.
It is responsible for:

Creating and managing vector indexes

Storing dense embeddings

Performing cosine similarity search

Returning top-k relevant chunks

3️⃣ Query Flow

User submits a question.

Question is converted into an embedding.

Endee retrieves the most similar chunks.

Retrieved context is passed to a local language model.

The model generates a grounded response.

4️⃣ API Layer

FastAPI exposes a /ask endpoint to interact with the assistant.
Interactive documentation is available via Swagger.

🗂️ Project Structure
mental-health-rag-endee/
│
├── src/
│   ├── ingest.py        # Embeds and stores data in Endee
│   ├── rag.py           # Retrieval + generation logic
│   ├── app.py           # FastAPI backend
│   ├── utils.py         # Text chunking utility
│   ├── test_search.py   # Semantic search testing
│   └── test_rag.py      # RAG testing
│
├── data/                # Mental health text dataset
├── endee-server/        # Docker setup for Endee
├── README.md
└── .gitignore
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/mental-health-rag-endee.git
cd mental-health-rag-endee
2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3️⃣ Start Endee Server (Docker Required)
cd endee-server
docker compose up -d

Endee runs locally at:

http://127.0.0.1:8080
4️⃣ Ingest Data into Endee
cd ../src
python ingest.py

This step:

Creates the vector index (if not already present)

Converts text into embeddings

Stores vectors inside Endee

5️⃣ Run the API Server
uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

Use the /ask endpoint to query the assistant.

🧪 Example Request
POST /ask

Request Body:

{
  "question": "How can I manage anxiety?"
}

The system will:

Retrieve relevant context from Endee

Generate a grounded response using the local model

🧠 Technical Stack

Python

FastAPI

SentenceTransformers

Transformers (local LLM)

Endee Vector Database

Docker

🔎 How Endee is Used in This Project

Endee serves as the core vector database.

Specifically, it is used to:

Create a vector index with cosine similarity

Store dense embeddings generated from text

Perform efficient nearest-neighbor search

Return top-k relevant chunks for RAG

All semantic search operations are executed through Endee’s index APIs.

This ensures:

Persistent storage

High-performance retrieval

Scalable architecture

Clear separation between storage and generation layers
