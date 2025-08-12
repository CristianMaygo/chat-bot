# API de Chatbot con Google Gemini

Esta es una API RESTful que permite interactuar con un chatbot inteligente potenciado por el modelo de lenguaje Gemini de Google.

## Funcionalidades

- Recibe preguntas de usuarios a través de una interfaz HTTP.
- Procesa las preguntas utilizando el modelo `gemini-2.5-flash(Por el momento)` de Google.
- Devuelve respuestas generadas por la inteligencia artificial.
- Implementa seguridad básica mediante una API Key (`X-API-Key`) para controlar el acceso.

## ¿Cómo usarla?

Para interactuar con el chatbot, envía una petición `POST` al endpoint `/chat/ask` incluyendo tu mensaje y una API Key válida en el encabezado `X-API-Key`, necesitas comunicarte conmigo para darte el API KEY, si clonas el repo tendrás que crear un archivo .env en la raiz del proyecto y agregar dos lineas de texto que son así:
- GEMINI_API_KEY=
- CHATBOT_API_KEY=
- 
En las cuales despues del guion en la primera pones la tuya y la segunda te doy la mía para que funcione el chatbot.

---

## Endpoints

### `POST /chat/ask`

**Descripción:**
Este endpoint permite enviar una pregunta al chatbot y obtener una respuesta generada por el modelo Gemini. Es el punto principal de interacción con la inteligencia artificial.

**Requiere autenticación:** Sí (mediante `X-API-Key` en los encabezados).

**Cuerpo de la Solicitud (Request Body):**
Se espera un objeto JSON con el siguiente formato:
```json
{
  "message": "string"
}
```
- `message` (string): El texto de la pregunta o prompt que se desea enviar al chatbot.

**Ejemplo de Solicitud:**
```json
{
  "message": "¿Cuál es la capital de Francia?"
}
```

**Cuerpo de la Respuesta (Response Body):**
Devuelve un objeto JSON con la respuesta del chatbot:
```json
{
  "response": "string"
}
```
- `response` (string): El texto de la respuesta generada por el modelo Gemini.

**Ejemplo de Respuesta Exitosa (Status 200 OK):**
```json
{
  "response": "La capital de Francia es París."
}
```

**Posibles Respuestas de Error:**
- `401 Unauthorized`: Si la `X-API-Key` no es proporcionada o es inválida.
- `422 Unprocessable Entity`: Si el formato de la solicitud es incorrecto (ej. `message` no es un string).
- `500 Internal Server Error`: Si ocurre un problema al comunicarse con la API de Gemini o un error interno del servidor.

---

## Modelos de Datos (Schemas)

### `ChatRequest`
Representa la estructura de la solicitud que se envía al chatbot.
```python
class ChatRequest(BaseModel):
    message: str
```
- `message` (string): El texto de la pregunta o prompt que se desea enviar al chatbot.

### `ChatResponse`
Representa la estructura de la respuesta que se recibe del chatbot.
```python
class ChatResponse(BaseModel):
    response: str
```
- `response` (string): El texto de la respuesta generada por el modelo Gemini.

### Para usar tu API localmente (mientras el servidor Uvicorn está corriendo), aquí tienes los enlaces:
  Activa tu entorno virtual y corre este comando:
  *  python -m uvicorn app.main:app --reload --port 8001
  ### Despues de esto puedes probar los dos siguientes links, el primero es para probar localmente el chatbot
   * Documentación Interactiva (Swagger UI):
      http://127.0.0.1:8001/docs
   * Documentación Alternativa (ReDoc):
      http://127.0.0.1:8001/redoc
### Enpoint:
  * Endpoint del Chatbot (para enviar preguntas):
      http://127.0.0.1:8001/chat/ask

  ## Nota: Recuerda que el puerto (8001 en este caso) puede variar si lo inicias con otro puerto (ej. --port 8000).

## Contacto

Comunícate conmigo mediante correo si necesitas usarla, o por medio de GitHub.

- **Email:** [maygo782@gmail.com](mailto:maygo782@gmail.com)
