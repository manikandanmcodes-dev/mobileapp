from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from groq import Groq
import settings
from services.prompt import SYSTEM_PROMPT
from database.chromadb import save_memory, get_memory

router = APIRouter()

client = Groq(api_key=settings.GROQ_API_KEY)


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    try:
        # Retrieve memory related to user message
        memory = get_memory(request.message)

        response = client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "system", "content": f"Previous memories about Sanji:\n{memory}"},
                {"role": "user", "content": request.message}
            ]
        )

        reply = response.choices[0].message.content

        # Save conversation to memory
        save_memory(f"Sanji: {request.message}")
        save_memory(f"Nova: {reply}")

        return {"reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))