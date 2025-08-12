from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
    "http://localhost",
    "http://localhost:8000", # Si usas el puerto 8000
    "http://localhost:8001", # Si usas el puerto 8001 (el que estamos usando)
    "http://localhost:5500", # El puerto común de Live Server para tu index.html
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:5500",
    # Puedes añadir más orígenes si tu frontend se despliega en otro dominio/puerto
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat", tags=["Chatbot"])

@app.get("/")
def read_root():
    """
    Este es el endpoint raíz de la API.
    Sirve como confirmacion para saber si la API funciona.
    """
    return{"message": "BIENVENIDO Al CHATBOT"}