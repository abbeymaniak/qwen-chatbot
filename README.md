## Qwen Chatbot API (`server.py`)

This project provides a FastAPI backend for a chatbot powered by the Qwen 2.5 model via the Ollama API which can be used by any model all thats needed is to reference the model to use.

### Features

- **Chat Endpoint**:  
	`POST /chat`  
	Accepts a JSON payload with a user message and returns the chatbot's response.

- **Home Endpoint**:  
	`GET /`  
	Returns a simple status message to verify the API is running.

- **CORS Support**:  
	CORS is enabled for all origins, allowing frontend applications to interact with the API.

### Example Usage

**Chat Request:**
```http
POST /chat
Content-Type: application/json

{
	"message": "Hello, chatbot!"
}
```

**Chat Response:**
```json
{
	"response": "Hello! How can I help you today?"
}
```

### Requirements

- Python 3.9+
- FastAPI
- Ollama
- Pydantic

### Running the Server

1. Install dependencies:
	 ```
	 pip install fastapi uvicorn ollama pydantic
	 ```
2. Start the server:
	 ```
	 uvicorn server:app --reload
	 ```
