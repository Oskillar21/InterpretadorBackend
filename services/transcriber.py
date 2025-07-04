# services/transcriber.py

import whisper

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe el contenido de un archivo de audio usando Whisper.
    
    :param audio_path: Ruta del archivo .mp3
    :return: Texto transcrito
    """
    model = whisper.load_model("base") 

    result = model.transcribe(audio_path, fp16=False)  
    text = result["text"]
    if not isinstance(text, str):
        text = " ".join(map(str, text))
    return text
