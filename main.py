import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurar FFmpeg antes de importar otras dependencias
import config

from fastapi import FastAPI
from routes.uploadRoutes import router as upload_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

app = FastAPI(
    title="Interpretador de Video",
    description="API para recibir un video, extraer el audio y transcribir su contenido.",
    version="1.0.0"
)

# Incluir rutas
app.include_router(upload_router, prefix="/api", tags=["Transcripción"])

@app.get("/")
async def root():
    return {"message": "API de Interpretación de Video activa"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes limitarlo si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)