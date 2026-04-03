from openai import OpenAI
import requests

openai_client = OpenAI()


def speech_to_text(audio_binary):
    response = openai_client.audio.transcriptions.create(
        model="whisper-1",
        file=("audio.wav", audio_binary, "audio/wav")
    )
    return response.text


def text_to_speech(text, voice="alloy"):
    response = openai_client.audio.speech.create(
        model="tts-1",
        voice=voice if voice else "alloy",
        input=text
    )
    return response.content


def openai_process_message(user_message):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant. Keep responses concise and clear."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
