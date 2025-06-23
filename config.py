import os

# Configurar ruta de FFmpeg
FFMPEG_PATH = r"C:\Users\oscar\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"

# Verificar que FFmpeg existe
if os.path.exists(FFMPEG_PATH):
    # Configurar variable de entorno para moviepy
    os.environ["FFMPEG_BINARY"] = FFMPEG_PATH
    print(f"FFmpeg configurado en: {FFMPEG_PATH}")
else:
    print(f"Advertencia: No se encontró FFmpeg en: {FFMPEG_PATH}")
    print("Verificando si FFmpeg está en PATH...")
    import shutil
    ffmpeg_in_path = shutil.which('ffmpeg')
    if ffmpeg_in_path:
        os.environ["FFMPEG_BINARY"] = ffmpeg_in_path
        print(f"FFmpeg encontrado en PATH: {ffmpeg_in_path}")
    else:
        print("FFmpeg no está disponible. Por favor, instálalo.")