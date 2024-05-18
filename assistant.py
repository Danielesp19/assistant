import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time


def speak(message):
    tts = gTTS(text=message, lang="es", slow=False)
    # filename = os.path.dirname(__file__) + "\\voice.mp3"
    filename = os.path.dirname(__file__) + "\\voice.mp3"
    tts.save(filename)
    time.sleep(0.1)
    playsound.playsound(filename)
    os.remove(filename)


def listen_with_retry(prompt):
        while True:
            speak(prompt)
            try:
                response = listen()
                return response
            except Exception as e:
                speak("No entendí lo que dijiste. Por favor, intenta de nuevo.")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening ...")
        beep()
        
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language='es-ES')
        except Exception as e:
            raise Exception(f"Exception: {str(e)}")
    return said


def beep():
    # filename = os.path.dirname(__file__) + "\\sounds\\beep.mp3"
    filename = os.path.dirname(__file__) + "\\sounds\\beep.mp3"
    playsound.playsound(filename)



