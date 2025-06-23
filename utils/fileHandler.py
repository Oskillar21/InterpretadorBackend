# utils/fileHandler.py

import os
from uuid import uuid4
from fastapi import UploadFile

def save_upload_file(upload_file: UploadFile, destination_dir: str = "temp") -> str:
    """
    Guarda el archivo subido en una carpeta temporal y devuelve su ruta.
    """
    os.makedirs(destination_dir, exist_ok=True)

    # Crear nombre único para evitar conflictos
    filename = upload_file.filename or ""
    file_extension = os.path.splitext(filename)[1]
    saved_name = f"{uuid4().hex}{file_extension}"
    saved_path = os.path.join(destination_dir, saved_name)

    # Guardar el archivo
    with open(saved_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return saved_path
