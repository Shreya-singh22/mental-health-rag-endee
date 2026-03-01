from sentence_transformers import SentenceTransformer
from endee import Endee
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# -------- Embedding Model --------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# -------- Local LLM --------
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
llm_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# -------- Connect to Endee --------
db = Endee()
db.set_base_url("http://127.0.0.1:8080/api/v1")
index = db.get_index("mental_health_index")


def retrieve_context(query, top_k=3):
    query_embedding = embedding_model.encode(query).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=top_k
    )

    context = "\n\n".join([r["meta"]["text"] for r in results])
    return context


def generate_answer(query):
    context = retrieve_context(query)

    prompt = f"""
Answer the question using only the provided context.
If context is insufficient, say so clearly.

Context:
{context}

Question:
{query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = llm_model.generate(
        **inputs,
        max_length=256,
        temperature=0.3
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer