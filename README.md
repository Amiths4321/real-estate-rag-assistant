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

git clone https://github.com/YOUR-USERNAME/real-estate-rag-assistant.git
cd real-estate-rag-assistant

**2. Install dependencies**
pip install -r requirements.txt

**3. Add your PDF documents**
Place your RERA / property PDFs inside the documents/ folder

**4. Install Ollama and pull IBM Granite**
ollama pull ibm/granite3.2-vision:2b

**5. Run ingestion**
python ingest.py

**6. Launch the app**
streamlit run app.py

---

## Architecture
User Question
│
▼
Streamlit UI (app.py)
│
▼
RAG Pipeline (rag.py)
│
├── ChromaDB → finds top 4 relevant chunks
│
└── IBM Granite (Ollama) → generates answer with citations

---

## About the Author

AI Engineer with 20+ years experience across Real Estate, IBM API 
Integration, DevOps and Generative AI. This project combines domain 
expertise with hands-on AI engineering.

LinkedIn: [your-linkedin-url]

**1. Clone the repo**

git clone https://github.com/YOUR-USERNAME/real-estate-rag-assistant.git
cd real-estate-rag-assistant

**2. Install dependencies**
pip install -r requirements.txt

**3. Add your PDF documents**
Place your RERA / property PDFs inside the documents/ folder

**4. Install Ollama and pull IBM Granite**
ollama pull ibm/granite3.2-vision:2b

**5. Run ingestion**
python ingest.py

**6. Launch the app**
streamlit run app.py

---

## Architecture
User Question
│
▼
Streamlit UI (app.py)
│
▼
RAG Pipeline (rag.py)
│
├── ChromaDB → finds top 4 relevant chunks
│
└── IBM Granite (Ollama) → generates answer with citations

---

## About the Author

AI Engineer with 20+ years experience across Real Estate, IBM API 
Integration, DevOps and Generative AI. This project combines domain 
expertise with hands-on AI engineering.

LinkedIn: [your-linkedin-url]


