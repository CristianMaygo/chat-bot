from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import get_gemini_response
from app.security.auth import get_api_key

router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post("/ask", response_model=ChatResponse)
def ask_chatbot(request: ChatRequest):
    """
    Endpoint para enviar una pregunta al chatbot y obtener una respuesta.
    Recibe un mensaje y devuelve la respuesta generada por la IA.
    Ahora soporta historial de conversación.
    """
    user_message = request.message
    session_id = request.session_id
    history = request.history
    
    gemini_response_data = get_gemini_response(user_message, session_id, history)
    
    return ChatResponse(
        response=gemini_response_data["response"],
        session_id=session_id,
        history=gemini_response_data["history"]
        )