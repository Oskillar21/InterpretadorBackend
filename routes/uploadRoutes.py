# routes/uploadRoutes.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from controllers.uploadController import handle_video_upload

router = APIRouter()

# Ruta para subir un video y procesarlo
@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    result = handle_video_upload(file)
    return JSONResponse(content=result)