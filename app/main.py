from fastapi import FastAPI
from app.api.endpoints import chat

app = FastAPI(
    title="Chatbot API con Gemini",
    version="1.0",
    description="Una API que interactua con un chatbot potenciado usando IA"
)

app.include_router(chat.router, prefix="/chat", tags=["Chatbot"])

@app.get("/")
def read_root():
    """
    Este es el endpoint raíz. Este devuelve un simple saludo de bievenida.
    Es necesario, ya que este comprueba que la API funciona.
    """
    return{"message": "Bienvenido al ChatBot"}
pass