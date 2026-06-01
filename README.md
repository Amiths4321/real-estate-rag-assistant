# 🏠 Real Estate RAG Assistant

An AI-powered chatbot that answers Indian real estate and RERA compliance 
questions using Retrieval-Augmented Generation (RAG).

Built by someone with 14 years of Real Estate domain experience — 
the questions and documents are chosen by a practitioner, not just a developer.

---

## What it does

- Answers natural language questions over RERA, MahaRERA and property documents
- Cites the exact source document for every answer
- Runs fully locally — no paid API keys required
- Processes any new PDF documents automatically

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | IBM Granite 3.2 Vision (via Ollama) |
| RAG Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| UI | Streamlit |
| Language | Python 3.12 |

---

## Sample Questions it Answers

- "What are RERA registration requirements for a developer?"
- "What is the penalty for project delay under RERA?"
- "What is the carpet area definition under RERA?"
- "What documents does a buyer need for due diligence?"

---

## How to Run Locally

**1. Clone the repo**
