def chunk_text(documents, chunk_size=1000, overlap=250):
    chunks = []

    for doc in documents:
        text = doc["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "source": doc["source"],
                "page": doc["page"]
            })

            start += chunk_size - overlap

    return chunks

