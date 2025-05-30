import speech_recognition as sr
from gtts import gTTS
import os
from app.assistant import get_answer

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # On Linux use "mpg123 response.mp3"

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak your coding question:")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"🔎 You said: {query}")
        return query
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Sorry, there's a problem with the speech recognition service."

if __name__ == "__main__":
    question = listen()
    answer = get_answer(question)
    print(f"🤖 Assistant: {answer}")
    speak(answer)
