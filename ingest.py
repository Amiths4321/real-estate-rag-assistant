import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

load_dotenv()

docs_folder = "documents"
all_docs = []

for filename in os.listdir(docs_folder):
    if filename.endswith(".pdf"):
        path = os.path.join(docs_folder, filename)
        loader = PyPDFLoader(path)
        docs = loader.load()
        for doc in docs:
            doc.metadata["source_file"] = filename
        all_docs.extend(docs)
        print(f"Loaded: {filename} ({len(docs)} pages)")

print(f"Total pages loaded: {len(all_docs)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=80
)
chunks = splitter.split_documents(all_docs)
print(f"Created {len(chunks)} chunks")

embeddings = OllamaEmbeddings(
    base_url="http://10.22.39.192:11434",
    model="ibm/granite3.2-vision:2b"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./db"
)
print("Stored in ChromaDB successfully!")

results = vectorstore.similarity_search("RERA registration", k=2)
print("\nTest search:")
for r in results:
    print(f"  [{r.metadata['source_file']}] {r.page_content[:150]}")