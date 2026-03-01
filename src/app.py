from fastapi import FastAPI
from pydantic import BaseModel
from rag import generate_answer

app = FastAPI(title="Mental Health RAG Assistant")

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    answer = generate_answer(request.question)
    return {"answer": answer}