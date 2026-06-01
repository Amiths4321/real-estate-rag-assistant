import os
import json
import requests
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

load_dotenv()

OLLAMA_URL = "http://10.22.39.192:11434/api/generate"
QWEN_MODEL = "ibm/granite3.2-vision:2b"

def load_vectorstore():
    embeddings = OllamaEmbeddings(
    base_url="http://10.22.39.192:11434",
    model="ibm/granite3.2-vision:2b"
)
    return Chroma(
        persist_directory="./db",
        embedding_function=embeddings
    )

def ask_model(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": QWEN_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 800,
                    "num_ctx": 4096
                }
            },
            timeout=180
        )

        if response.status_code != 200:
            return f"Server error {response.status_code}: {response.text[:200]}"

        raw = response.text.strip()

        if raw.count("{") > 1:
            full_answer = ""
            for line in raw.split("\n"):
                line = line.strip()
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                    full_answer += chunk.get("response", "")
                    if chunk.get("done", False):
                        break
                except:
                    continue
            return full_answer.strip()

        data = json.loads(raw)
        return data.get("response", "No response received").strip()

    except requests.exceptions.Timeout:
        return "Error: Request timed out — try again."
    except requests.exceptions.ConnectionError:
        return f"Error: Cannot reach Ollama at {OLLAMA_URL}"
    except json.JSONDecodeError as e:
        return f"JSON error: {e}\nRaw: {response.text[:300]}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def ask_question(question: str, vectorstore) -> dict:
    results = vectorstore.similarity_search(question, k=4)

    if not results:
        return {
            "answer": "No relevant documents found.",
            "sources": [],
            "chunks_used": 0
        }

    context_parts = []
    sources = set()
    for i, r in enumerate(results):
        src = r.metadata.get("source_file", "unknown")
        sources.add(src)
        context_parts.append(f"[Source {i+1}: {src}]\n{r.page_content}")

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are an expert Real Estate Assistant specializing in
Indian real estate law, RERA regulations, and Mumbai property markets.

Use ONLY the information in the CONTEXT below to answer the question.
Always mention which source document your answer is from.
If the answer is not found in the context, say:
"This information is not available in my documents."

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""

    answer = ask_model(prompt)

    return {
        "answer": answer,
        "sources": list(sources),
        "chunks_used": len(results)
    }


if __name__ == "__main__":
    print("Loading vectorstore...")
    vs = load_vectorstore()
    print("Vectorstore loaded.\n")

    questions = [
        "What are RERA registration requirements for a developer?",
        "What is the penalty for project delay under RERA?",
    ]

    for q in questions:
        print(f"Q: {q}")
        result = ask_question(q, vs)
        print(f"A: {result['answer'][:400]}")
        print(f"Sources: {result['sources']}")
        print("-" * 60)