import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config  # Importar configuración de FFmpeg
from moviepy import VideoFileClip 
from uuid import uuid4

def extractAudioFromVideo(video_path: str, output_dir: str = "temp") -> str:
    print(f"🎬 Iniciando extracción de audio de: {video_path}")
    
    # Verificar que el video existe
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"El archivo de video no existe: {video_path}")
    
    # Crear carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 Carpeta de salida: {os.path.abspath(output_dir)}")

    # Generar nombre único
    audio_filename = f"{uuid4().hex}.mp3"
    audio_path = os.path.join(output_dir, audio_filename)
    print(f"🎵 Archivo de audio a crear: {audio_path}")

    try:
        # Extraer audio
        print("🔄 Iniciando VideoFileClip...")
        with VideoFileClip(video_path) as video:
            print("✅ VideoFileClip creado exitosamente")
            audio = video.audio
            if audio is None:
                raise ValueError("No se pudo extraer audio del video.")
            print("🎵 Audio extraído, escribiendo archivo...")
            audio.write_audiofile(audio_path, logger=None)
            print("✅ Archivo de audio creado exitosamente")

        return audio_path
    
    except Exception as e:
        print(f"❌ Error en extractAudioFromVideo: {e}")
        print(f"❌ Tipo de error: {type(e).__name__}")
        raise