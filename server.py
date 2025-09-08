from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama


app = FastAPI()

#enable CORS to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify ["http://localhost:3000"] for local development)
    allow_credentials=True,
    allow_methods=["*"], #Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ollama.chat(model="qwen2.5", messages=[{"role": "user", "content": request.message}])
        return {"response": response['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/")
def home():
    return {"message": "Qwen 2.5 chatbot API is running."}