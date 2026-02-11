# DocSense AI

DocSense AI is a full-stack conversational document assistant that allows users to upload PDF documents and interact with them using a hybrid Retrieval-Augmented Generation (RAG) pipeline.

It combines dense vector search (FAISS) and sparse keyword search (TF-IDF) with a large language model to provide grounded, source-aware responses.

---

<img width="1905" height="881" alt="{F95F49C8-DC76-405E-8ECE-8D7DE48C8A2C}" src="https://github.com/user-attachments/assets/a473cd5d-a101-4a46-b8ac-d9b6ab15b873" />

##  Features

- PDF Upload & Dynamic Indexing
- Hybrid Retrieval (Dense + Sparse Search)
- Conversational Memory
- Background Indexing with Status Tracking
- ChatGPT-style React UI
- FastAPI Backend
- Groq LLM Integration
- Markdown Rendering & Dark Mode UI

---

##  Architecture

Frontend (React + Vite)  
→ REST API  
→ FastAPI Backend  
→ Hybrid Retrieval (FAISS + TF-IDF)  
→ Groq-hosted LLM  

---

##  Tech Stack

### Frontend
- React (Vite)
- Axios
- React Markdown

### Backend
- FastAPI
- FAISS
- Sentence Transformers
- Scikit-learn (TF-IDF)
- Groq API
- Background Tasks

---


---

##  Running the Project

###  Backend

cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs at:
http://127.0.0.1:8000


---

###  Frontend

cd frontend
npm install
npm run dev


Frontend runs at:


http://localhost:5173


---



## 👨‍💻 Developed By 
@Sumit Saurabh
