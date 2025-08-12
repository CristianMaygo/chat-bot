import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(override=True)

class Settings(BaseSettings):
    """
    Clase para menajar la config de la app.
    Las variables de entorno se cargan automaticamente.
    """
    GEMINI_API_KEY: str
    
    CHATBOT_API_KEY: str
    
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    
settings = Settings()
