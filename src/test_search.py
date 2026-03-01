from sentence_transformers import SentenceTransformer
from endee import Endee

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Endee
db = Endee()
db.set_base_url("http://127.0.0.1:8080/api/v1")

index = db.get_index("mental_health_index")

query = "How to deal with anxiety?"
query_embedding = model.encode(query).tolist()

results = index.query(
    vector=query_embedding,
    top_k=3
)

print("\n🔍 Top Results:\n")

for r in results:
    print("Similarity:", r["similarity"])
    print("Text:", r["meta"]["text"])
    print("-" * 50)