import uvicorn
import socketio
from contextlib import asynccontextmanager
from loguru import logger
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from llmbuddy.controllers.models_controller import router as models_router
from llmbuddy.controllers.chat_controller import router as chat_router
from llmbuddy.controllers.documents_controller import router as document_router
from llmbuddy.services.llm.gemini_service import GeminiService
from llmbuddy.services.agent.supervisor_agent import SupervisorAgent
from llmbuddy.services.agent.weather_agent import WeatherAgent

origins = [
    "http://localhost:5173"
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init LLM
    app.state.var = {}
    app.state.var['llm'] = GeminiService(model_name="gemini-2.0-flash")
    try:
        app.state.var['agent'] = SupervisorAgent(
            model=app.state.var['llm'],
            agents=[
                WeatherAgent(app.state.var['llm'])(), 
            ]
        )
        logger.info("Load model successfully!")
    except: 
        logger.error("Unable to load model!")
    
    yield
    app.state.var.clear()

app = FastAPI(
    title="OpenAgents WebUI",
    docs_url="/docs",
    openapi_url="/openapi.json",
    redoc_url=None,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sio = socketio.AsyncServer(
    cors_allowed_origins=origins,
    async_mode="asgi",
    transports=(["websocket"]),
    allow_upgrades=True,
    always_connect=True,
)

socket_app = socketio.ASGIApp(
    sio,
    socketio_path="/ws/socket.io",
)
app.mount("/ws", socket_app)
app.include_router(models_router, prefix="/models", tags=["models"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(document_router, prefix="/document", tags=["document"])

@app.post("/api/v1/auths/signin")
async def sign_in():
    return {
            "token": '',
            "token_type": "Bearer",
            "expires_at": '',
            "id": '',
            "email": '',
            "name": '',
            "role": 'admin',
            "profile_image_url": '',
            "permissions": '',
        }

@app.get("/api/v1/channels")
async def channels():
    return {}

@app.get("/api/config")
async def get_config():
    return {
        **({"onboarding": True}),
        "status": True,
        "name": "Open WebUI",
        "version": "0.6.10",
        "default_locale": "",
        "oauth": {
            "providers": {}
        },
        "features": {
            "auth": False,
            "auth_trusted_header": False,
            "enable_ldap": True,
            "enable_api_key": False,
            "enable_signup": False,
            "enable_login_form": False,
            "enable_websocket": True,
            **(
                {
                    "enable_direct_connections": True,
                    "enable_channels": True,
                    "enable_notes": True,
                    "enable_web_search": True,
                    "enable_code_execution": True,
                    "enable_code_interpreter": True,
                    "enable_image_generation": True,
                    "enable_autocomplete_generation": True,
                    "enable_community_sharing": True,
                    "enable_message_rating": True,
                    "enable_user_webhooks": True,
                    "enable_admin_export": True,
                    "enable_admin_chat_access": True,
                    "enable_google_drive_integration": True,
                    "enable_onedrive_integration": True,
                }
            ),
        },
        **(
            {
                "default_models": None,
                "default_prompt_suggestions": [],
                "user_count": 1,
                "code": {
                    "engine": 'pyodide',
                },
                "audio": {
                    "tts": {
                        "engine": '',
                        "voice": 'alloy',
                        "split_on": 'punctuation',
                    },
                    "stt": {
                        "engine": '',
                    },
                },
                "file": {
                    "max_size": None,
                    "max_count": None,
                },
                "permissions": {},
                "google_drive": {
                    "client_id": '',
                    "api_key": '',
                },
                "onedrive": {
                    "client_id": '',
                    "sharepoint_url": '',
                    "sharepoint_tenant_id": '',
                },
                "ui": {
                    "pending_user_overlay_title": '',
                    "pending_user_overlay_content": '',
                    "response_watermark": '',
                },
                "license_metadata": None,
                **(
                    {
                        "active_entries": 0,
                    }
                ),
            }
        )
    }

@app.get("/static/favicon.png")
async def get_static():
    pass

if __name__ == "__main__":
    uvicorn.run("llmbuddy.main:app", host="localhost", port=8080, reload=True)