import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(prompt: str) -> str:
    """
    Envía un prompt a la IA y este devuelve una respuesta.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error al obtener la respuesta de la IA: {e}")
        return "Lo siento, no pude procesar tu solicitud en este momento."