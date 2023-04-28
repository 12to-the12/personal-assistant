
import speech_recognition as sr
# import sys
import os
# import warnings
import contextlib
import io
import time
from play import play
# import pydub
import time

from config import config




if config["local_transcription"]:
    print('loading model...')
    model_name = config["recognition_model"]
    import whisper
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
#     sys.stdout = open(os.devnull, 'w')

# # Restore
# def enablePrint():
#     sys.stdout = sys.__stdout__
 

r = sr.Recognizer()
m = sr.Microphone()


def save_audio(audio_file):
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
    except:
        print(f"Waiting to adjust until audio recording stops")


def record():
    print("Say something!")
    play('listening.mp3', asyncronous=False)
    try:
        with m as source:
            audio = r.listen(source, timeout=5)
    except: print("couldn't record audio")
    # save the audio data to a file

    play("stopped-listening.mp3")
    save_audio(audio)

    print("Got it! Now to recognize it...")
    return audio

    


def recognize_audio(audio=None):
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
            print("An audio recognition error occured:", e)
            continue
    print("complete!")

    return text


if __name__ == "__main__":
    # adjust the noise once at the beginning of the session
    print("A moment of silence, please...")
    adjust_noise()

    # start the recognition loop
    text = recognize()
    # audio = record()
    # print('transcripting...')
    # text = recognize_audio('xx')
    # print('done')

    print(f"You said: {text}")

# if __name__ == "__main__":
#     audio = pydub.AudioSegment.from_file("dictation 1682508402.834191.mp3", format="mp3")
#     print(recognize_audio(audio))
