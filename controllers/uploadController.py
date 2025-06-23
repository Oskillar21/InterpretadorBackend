from fastapi import UploadFile
from utils.fileHandler import save_upload_file
from services.audioExtractor import extract_audio_from_video
from services.transcriber import transcribe_audio
from services.resume import resumeText

def handle_video_upload(file_path: str):
    transcript = transcribe_audio(file_path)
    summary = resumeText(transcript)
    return {
        "transcription": transcript,
        "summary": summary
    }

def handle_video_upload(file: UploadFile) -> dict:
    try:
        # Guardar video
        video_path = save_upload_file(file)

        # Extraer audio
        audio_path = extract_audio_from_video(video_path)

        # Transcribir audio
        transcript = transcribe_audio(audio_path)

        return {
            "message": "Transcripción exitosa",
            "transcription": transcript,
            "video_path": video_path,
            "audio_path": audio_path
        }

    except Exception as e:
        return {
            "error": f"Error al procesar el video: {str(e)}"
        }