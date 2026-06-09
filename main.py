from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI"}
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "role": "assistant",
        "content": f"「{req.message}」を受け取りました。"
    }

