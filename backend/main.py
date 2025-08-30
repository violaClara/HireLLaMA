from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from rag_utils import process_cv_file, answer_question
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "./cv_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_cv(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    process_cv_file(path)
    return {"status": "uploaded", "filename": file.filename}

@app.post("/ask/")
async def ask_ai(question: str = Form(...)):
    result = answer_question(question)
    return {"response": result}
