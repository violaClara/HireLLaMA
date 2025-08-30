# ⚡ HireLLaMA (LLaMA + RAG)

An AI-powered assistant that helps recruiters summarize resumes, extract skills, and answer queries about candidates.  
Built with **LLaMA (via Ollama)**, **ChromaDB**, and **SentenceTransformers**  this project demonstrates how open-source AI can streamline hiring.

---

##  Key Features
-  **Resume Parsing**: Extract text from PDF CVs using `pdfplumber`.
-  **Semantic Search**: Store and retrieve CVs via **ChromaDB** with embeddings from `SentenceTransformers`.
-  **AI Summarization**: Use **LLaMA (Ollama)** to generate concise summaries of candidate CVs.
-  **Recruiter Q&A**: Ask natural language questions (e.g., *"Who has strong Python and data analysis skills?"*) and get tailored answers.
-  **Scalable Architecture**:  easily extendable to production.

---

##  Tech Stack
- **Frontend**: Next.js + TailwindCSS (Recruiter Dashboard)
- **Backend**: FastAPI (Python)
- **AI Model**: Meta LLaMA (via Ollama)
- **Vector Database**: ChromaDB
- **Embeddings**: SentenceTransformers (all-MiniLM-L6-v2)
- **PDF Parsing**: pdfplumber
- **Deployment**: Local 

---


