def chunk_text(text, chunk_size=200):
    """
    Splits text into smaller chunks of words.
    This helps embeddings work better.
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks