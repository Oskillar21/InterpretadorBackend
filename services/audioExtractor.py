import os
from moviepy import VideoFileClip 
from uuid import uuid4

def extractAudioFromVideo(video_path: str, output_dir: str = "temp") -> str:
  
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