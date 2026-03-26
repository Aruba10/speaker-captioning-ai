import speech_recognition as sr
import librosa
import soundfile as sf
import os

# ---------- AUDIO PATH ----------
audio_path = "audio/test.wav"

print("\n🔊 Processing Audio...\n")

# ---------- LOAD AUDIO ----------
try:
    y, sr_rate = librosa.load(audio_path, sr=None)
except Exception as e:
    print("❌ Error loading audio file:", e)
    exit()

# ---------- SEGMENT SETTINGS ----------
segment_duration = 4  # seconds
samples_per_segment = int(segment_duration * sr_rate)

recognizer = sr.Recognizer()
speaker_toggle = 1

# ---------- PROCESS EACH SEGMENT ----------
for start in range(0, len(y), samples_per_segment):
    end = start + samples_per_segment

    segment_file = f"temp_{start}.wav"

    # Save segment
    sf.write(segment_file, y[start:end], sr_rate)

    try:
        with sr.AudioFile(segment_file) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        print(f"Speaker {speaker_toggle}: {text}")

        # Toggle speaker
        speaker_toggle = 2 if speaker_toggle == 1 else 1

    except sr.UnknownValueError:
        print(f"Speaker {speaker_toggle}: [Could not understand]")

    except sr.RequestError:
        print(f"Speaker {speaker_toggle}: [API error]")

    finally:
        # Delete temp file
        if os.path.exists(segment_file):
            os.remove(segment_file)

print("\n✅ Processing Completed!\n")
