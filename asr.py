import speech_recognition as sr
import soundfile as sf
import os

recognizer = sr.Recognizer()

def convert_speech(segment, sr_rate, filename):
    sf.write(filename, segment, sr_rate)

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

    except:
        text = "[Could not understand]"

    finally:
        if os.path.exists(filename):
            os.remove(filename)

    return text
