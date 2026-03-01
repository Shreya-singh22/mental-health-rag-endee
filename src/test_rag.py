from rag import generate_answer

query = "How can I manage anxiety naturally?"

answer = generate_answer(query)

print("\n🧠 Local RAG Response:\n")
print(answer)