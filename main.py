from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env in dev (Render will inject vars directly in prod)
load_dotenv()

# Initialize app + client
app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TextIn(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Summarizer API 🚀"}

@app.get("/health")
def healthcheck():
    return {"status": "ok", "message": "API is healthy!"}

@app.post("/summarize")
def summarize(data: TextIn):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize: {data.text}"}]
    )
    return {"summary": response.choices[0].message.content}
