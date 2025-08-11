from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import get_gemini_response

router = APIRouter()

@router.post("/ask", response_model=ChatResponse)
def ask_chatbot(request: ChatRequest):
    """
    Endpoint para enviar una pregunta al chatbot y obtener una respuesta.
    Recibe un mensaje y devuelve la respuesta generada por la IA.
    """
    user_message = request.message
    gemini_response = get_gemini_response(user_message)
    return ChatResponse(response=gemini_response)