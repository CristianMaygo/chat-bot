from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from app.core.config import settings

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=True)

def get_api_key(api_key: str = Security(api_key_header)):
    """
    Función de dependencia que verifica que la API Key proporcionada
    en el encabezado 'X-API-KEY' sea valida.
    """
    if api_key == settings.CHATBOT_API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="API KEY INVALIDA",
    )