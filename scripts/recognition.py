# this segment turns speech into text

# import sys
# import warnings
import contextlib
import os, time, logging, io


# import pydub

import speech_recognition as sr

from scripts.config import config
from scripts.play import play



if config["local_transcription"]:
    print('loading model...')
    model_name = config["recognition_model"]
    import whisper
    # see https://github.com/openai/whisper for usage
    model = whisper.load_model(model_name)
    print('model loaded...')

# # Define a filter that matches all warnings
# warnings.filterwarnings('ignore', category=Warning)

# # Redirect warnings to the null device
# warnings.filterwarnings('always', '', Warning)
# warnings.simplefilter('ignore')


# Redirect all output to the null device


os.close(2)
os.open(os.devnull, os.O_RDWR)


# # Disable
# def blockPrint():
#     syquit()

m = sr.Microphone()
r = sr.Recognizer()

def save_audio(audio_file):
    """saves an """
    # once for the archive
    filename = f"dictation {time.time()}.mp3"
    with open("dictation/"+filename, "wb") as f:
        f.write(audio_file.get_wav_data())

    # and the active copy
    filename = "speech.mp3"
    with open(filename, "wb") as f:
        f.write(audio_file.get_wav_data())


def adjust_noise():
    
    global r
    try:
        with m as source:
            r.adjust_for_ambient_noise(source, duration=1)
        print(f"Set energy threshold to {r.energy_threshold:.0f}")
    except Exception as e:
        print("An error occurred:", str(e))
        print(f"Waiting to adjust until audio recording stops")


def record():
    print("Say something!")
    play('audio-files/listening.mp3')
    # start suppressing output here
    try:
        with m as source:
            audio = r.listen(source, timeout=5)
    except Exception as e:
        print("An error occurred:", str(e))
        printf("couldn't record audio")
    # save the audio data to a file
    # stop suppressing output here
    play("audio-files/stopped-listening.mp3")
    save_audio(audio)

    print("Got it! Now to recognize it...")
    return audio

    



def recognize_audio(audio=None) -> str:
    """not a duplicate function, this function transcribes an audio file"""
    try:
        if config["local_transcription"]:
            global model
            save_audio(audio)
            result = model.transcribe("speech.mp3")
            # print(f"transcription: {end-start:.2f}s")
            return result["text"]
        
        else:
            with contextlib.redirect_stdout(io.StringIO()):
                result = r.recognize_google(audio)
                return result
            
    except sr.UnknownValueError as e:
        print("Oops! Didn't catch that")
        raise Exception("incomprehensible") from e
    except sr.RequestError as e:
        print(
            "Uh oh! Couldn't request results from Speech Recognition service; {0}".format(e))
        raise Exception("bad API") from e
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # delete the audio file
        # os.remove(filename)
        pass




def recognize():
    """records and transcribes audio"""
    print("in recognize")
    while 1:
        try:
            print('attempting to record')
            audio = record()
            
            print('recording succeeded')

        except Exception as e:
            print("A recording error occurred:", e)
            continue
        try:
            print('attempting to recognize')
            text = recognize_audio(audio)
            print('audio recognition succeeded')
            break
        except Exception as e:
            print("An audio recognition error occurred:", e)
            continue
    print("complete!")

    return text


