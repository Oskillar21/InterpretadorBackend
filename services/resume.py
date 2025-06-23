
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def resumeText(text: str) -> str:
    response = client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Eres un asistente que resume texto de manera clara y concisa."},
            {"role": "user", "content": f"Resume el siguiente texto:\n{text}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
