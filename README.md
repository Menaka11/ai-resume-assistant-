# AI Resume Assistant (RAG-based)

## 🚀 Overview

This project is an AI-powered Resume Assistant that allows users to query resume content and receive intelligent responses using semantic search and LLMs.

## 🧠 Features

* Resume-based question answering
* Semantic search using TF-IDF vectorization
* Context-aware responses using Groq API
* Lightweight and fast (no heavy model downloads)

## 🛠️ Tech Stack

* Python
* Scikit-learn (TF-IDF, Cosine Similarity)
* Groq API (LLM)

## ⚙️ How it Works

1. Loads resume text
2. Splits into chunks
3. Converts text into vectors
4. Finds relevant content based on query
5. Uses LLM to generate answers

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## 💬 Example Queries

* What are my skills?
* Summarize my resume
* Am I fit for a Java developer role?

## 📌 Future Improvements

* Add Streamlit UI
* Add job description matching
* Use advanced embeddings (FAISS)

## 👩‍💻 Author

Menaka M
