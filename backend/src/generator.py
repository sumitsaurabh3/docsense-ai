import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(query, retrieved_chunks, chat_history=None):
    context = ""
    sources = []

    for i, chunk in enumerate(retrieved_chunks):
        context += f"\n[Source {i+1}] (File: {chunk['source']}, Page: {chunk['page']})\n"
        context += chunk["text"] + "\n"
        sources.append(f"{chunk['source']} (Page {chunk['page']})")

    messages = []

    # System role
    messages.append({
        "role": "system",
        "content": "You are an intelligent document assistant. Answer strictly using the provided context."
    })

    # Add previous chat history
    if chat_history:
        messages.extend(chat_history)

    # Add current query with context
    messages.append({
        "role": "user",
        "content": f"""
Context:
{context}

Question:
{query}
"""
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content, sources
