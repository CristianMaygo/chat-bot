import google.generativeai as genai
from app.core.config import settings
from typing import List, Dict, Any
from app.schemas.chat import Message

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash',
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.3,
                                top_p=0.9,
                                top_k=40,
                            )
                        )

    # --- Almacenamiento en memoria para las sesiones de chat ---
    # IMPORTANTE: En un entorno de producción, esto debería ser una base de datos
    # o un caché persistente (como Redis) para que el historial no se pierda
    # si el servidor se reinicia o si hay múltiples instancias de la API.
active_chat_sessions: Dict[str, Any] = {} # Almacena objetos de chat de Gemini

def get_gemini_response(
    prompt: str,
    session_id: str,
    history: List[Message] = None
    ) -> Dict[str, Any]:
    """
    Envía un prompt a la IA y este devuelve una respuesta, manteniendo el historial.
    Si la sesión no existe, la crea, si existe, la usa.
    """
    try:
        print(f"DEBUG: Historial recibido del frontend para {session_id}: {history}")
        chat_session = active_chat_sessions.get(session_id)
        
        if not chat_session:
            initial_history = []
            if history:
                for msg in history:
                    initial_history.append({'role': msg.role, 'parts': [{'text': p} for p in msg.parts]})
                    
            chat_session = model.start_chat(history=initial_history)
            active_chat_sessions[session_id] = chat_session
            print(f"Nueva sesión de chat iniciada para ID: {session_id}")
        else:
            print(f"Sesión de chat existente para ID: {session_id}")
        
        response = chat_session.send_message(prompt)
        
        update_history = []
        for msg in chat_session.history:
            parts_text = [part.text for part in msg.parts if hasattr(part, 'text')]
            update_history.append({
                'role': msg.role,
                'parts': parts_text
            })
            
        return {
            "response": response.text,
            "history": update_history
        }
        
    except Exception as e:
        print(f"Error al obtener respuesta de Gemini para sesión {session_id}: {e}")
    return {
        "response": "Lo siento, no pude procesar tu solicitud en este momento. Por favor, intenta de nuevo.",
        "history": history if history else [] # Devolvemos el historial previo si lo teníamos
    }
        