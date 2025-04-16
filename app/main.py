from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="XM Automatización - Registro de Fronteras")

app.include_router(router)
