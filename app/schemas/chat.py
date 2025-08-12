from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str
    parts: List[str]

class ChatRequest(BaseModel):
    """
    Define la estructura de la solicitud (Pregunta) al chatbot.
    Incluye un session_id opcional y el historial de la conversación.
    """
    message: str
    session_id: Optional[str] = None
    history: Optional[List[Message]] = None

class ChatResponse(BaseModel):
    """
    Define la estructura de la respuesta del chatbot.
    """
    response: str
    session_id: Optional[str] = None
    history: Optional[List[Message]] = None