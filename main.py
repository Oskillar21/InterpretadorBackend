
from fastapi import FastAPI
from routes.uploadRoutes import router as upload_router

app = FastAPI(
    title="Interpretador de Video",
    description="API para recibir un video, extraer el audio y transcribir su contenido.",
    version="1.0.0"
)

# Incluir rutas
app.include_router(upload_router, prefix="/api", tags=["Transcripción"])

@app.get("/", tags=["Inicio"])
async def root():
    return {"message": "API de interpretación de video activa"}
