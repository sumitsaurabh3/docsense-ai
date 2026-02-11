from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from fastapi import BackgroundTasks
from src.retriever import Retriever
from src.generator import generate_answer
from src.vector_store import build_vector_store
from fastapi import BackgroundTasks
app = FastAPI(title="DocSense RAG API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = "data"
chat_sessions = {}
index_status = {"status": "idle"}
retriever = Retriever()

class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QueryRequest):
    session_id = "default"   # For now, single user

    if session_id not in chat_sessions:
        chat_sessions[session_id] = []

    results = retriever.retrieve(request.question)

    answer, sources = generate_answer(
        request.question,
        results,
        chat_history=chat_sessions[session_id]
    )

    # Store conversation
    chat_sessions[session_id].append({
        "role": "user",
        "content": request.question
    })
    chat_sessions[session_id].append({
        "role": "assistant",
        "content": answer
    })

    return {
        "answer": answer,
        "sources": sources
    }


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    file_path = os.path.join(DATA_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    index_status["status"] = "indexing"

    background_tasks.add_task(rebuild_index)

    return {"message": "File uploaded. Indexing started."}

def rebuild_index():
    global retriever
    build_vector_store()
    retriever = Retriever()
    index_status["status"] = "completed"

@app.get("/status")
def get_status():
    return {"status": index_status["status"]}