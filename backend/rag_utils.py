import pdfplumber
import chromadb
from sentence_transformers import SentenceTransformer
from ollama import Client
import os

client = Client(host='http://localhost:11434')
model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("cv_collection")

def extract_text(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join(p.extract_text() or '' for p in pdf.pages)

def process_cv_file(path):
    text = extract_text(path)
    embedding = model.encode([text])[0]
    collection.add(
        documents=[text],
        ids=[path],
        metadatas=[{"filename": os.path.basename(path)}]
    )

def answer_question(question, top_k=2):
    results = collection.query(query_texts=[question], n_results=top_k)
    docs = results["documents"][0]
    summaries = []
    for doc in docs:
        prompt = f"Ringkas isi CV ini dalam 2 kalimat. Please summarize this CV in 2 concise sentences. Use Bahasa Indonesia.\n{doc[:1000]}"
        res = client.generate(model="llama3", prompt=prompt)
        summaries.append(res["response"])

    context = "\n".join(summaries)
    final_prompt = f"Here is summarized data from candidate CVs:\n{context}\n\n Now, based on the above summaries, please answer this question (use professional tone in Bahasa Indonesia):\n{question}"
    output = client.generate(model="llama3", prompt=final_prompt)
    return output['response'].strip()
