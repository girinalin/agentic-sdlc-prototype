from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="Agentic SDLC FastAPI Backend")
app.include_router(api_router, prefix="/api")
