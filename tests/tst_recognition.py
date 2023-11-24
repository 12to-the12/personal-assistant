import speech_recognition as sr
from scripts.recognition import recognize_audio
import os

def test_recognize_audio():
    os.close(2)
    os.open(os.devnull, os.O_RDWR)
    with sr.AudioFile("audio-files/sample.mp3") as source:
        r = sr.Recognizer()
        audio = r.record(source)
        transcript = recognize_audio(audio)
        assert transcript.lower() == " this is an audio test."
