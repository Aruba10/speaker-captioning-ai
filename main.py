import speech_recognition as sr
import librosa
import numpy as np

# ---------- AUDIO PATH ----------
audio_path = "audio/test.wav"

print("Loading audio...")

# Load audio
y, sr_rate = librosa.load(audio_path, sr=None)

duration = len(y) / sr_rate
print("Audio Length:", round(duration, 2), "sec")


# ---------- SEGMENT AUDIO ----------
segment_duration = 3   # seconds per segment
samples_per_segment = int(segment_duration * sr_rate)

segments = []

for start in range(0, len(y), samples_per_segment):
    end = start + samples_per_segment
    segments.append(y[start:end])

print("Total Segments:", len(segments))


# ---------- SPEECH RECOGNITION ----------
recognizer = sr.Recognizer()

with sr.AudioFile(audio_path) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("\nFull Transcription:")
    print(text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("API unavailable")
