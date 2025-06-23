import os
from moviepy import VideoFileClip 
from uuid import uuid4

def extract_audio_from_video(video_path: str, output_dir: str = "temp") -> str:
    """
    Extrae el audio en formato MP3 de un video dado.

    :param video_path: Ruta del archivo de video.
    :param output_dir: Carpeta donde se guardará el archivo MP3.
    :return: Ruta del archivo MP3 generado.
    """
    # Crear carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Generar nombre único
    audio_filename = f"{uuid4().hex}.mp3"
    audio_path = os.path.join(output_dir, audio_filename)

    # Extraer audio
    with VideoFileClip(video_path) as video:
        audio = video.audio
        if audio is None:
            raise ValueError("No se pudo extraer audio del video.")
        audio.write_audiofile(audio_path)

    return audio_path
