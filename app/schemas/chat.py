from pydantic import BaseModel

class ChatRequest(BaseModel):
    """
    Define la estructura de la solicitud (Pregunta) al chatbot.
    """
    message: str

class ChatResponse(BaseModel):
    """
    Define la estructura de la respuesta del chatbot.
    """
    response: str