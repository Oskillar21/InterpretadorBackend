## Requisitos

- Python 3.10 o superior
- `ffmpeg` instalado en el sistema:
  - **Windows:** `winget install ffmpeg`
---

## Instalación del entorno

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# En Windows:
.\venv\Scripts\activate
# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar Whisper desde GitHub (opcional, si lo usás)
pip install git+https://github.com/openai/whisper.git


#IMPORTANTE, crear archivo .env con 
GROQ_API_KEY=apiKey

#ejecutar el proyecto
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

#Terminar el proceso
Secuencia completa:
Apagar servidor: Ctrl + C
Salir del venv: deactivate
