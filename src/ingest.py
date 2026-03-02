from sentence_transformers import SentenceTransformer
from endee import Endee, Precision
import os
from utils import chunk_text

# Connect to Endee
db = Endee()
db.set_base_url("http://127.0.0.1:8080/api/v1")

INDEX_NAME = "mental_health_index"

# Create index ONLY if it does not exist
index_info = db.list_indexes().get("indexes", [])

existing_names = [idx["name"] for idx in index_info]

if INDEX_NAME not in existing_names:
    print("Creating index...")
    db.create_index(
        name=INDEX_NAME,
        dimension=384,
        space_type="cosine",
        precision=Precision.FLOAT32
    )

# Get index
index = db.get_index(INDEX_NAME)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

data_folder = "../data"
vectors_to_insert = []

for file in os.listdir(data_folder):
    if file.endswith(".txt"):
        with open(os.path.join(data_folder, file), "r") as f:
            text = f.read()

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk).tolist()

            vectors_to_insert = []

for file in os.listdir(data_folder):
    if file.endswith(".txt"):
        with open(os.path.join(data_folder, file), "r") as f:
            text = f.read()

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk).tolist()

            vectors_to_insert.append({
                "id": f"{file}_{i}",
                "vector": embedding,
                "meta": {
                    "text": chunk,
                    "source": file
                }
            })

index.upsert(vectors_to_insert)

# Upsert correctly (positional argument)
index.upsert(vectors_to_insert)

print("✅ Data successfully stored in Endee!")
