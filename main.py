from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

from dotenv import load_dotenv
load_dotenv()


# Initialize app + client
app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TextIn(BaseModel):
    text: str

@app.post("/summarize")
def summarize(data: TextIn):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize: {data.text}"}]
    )
    return {"summary": response.choices[0].message.content}
