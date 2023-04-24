
import speech_recognition as sr
# import sys
import os
# import warnings
import contextlib
import io
import time
from play import play

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
    filename = f"dictation {time.time()}.mp3"
    with open(filename, "wb") as f:
        f.write(audio_file.get_wav_data())


def adjust_noise(ambient=None):
    global r
    # if this is passed a preset value, otherwise, sample
    if ambient:
        with m as source:
            r.adjust_for_ambient_noise(source, duration=1)
    else:
        with m as source:
            r.adjust_for_ambient_noise(source, duration=1)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))


def record():
    print("Say something!")
    play('listening.mp3', asyncronous=False)
    
    with m as source:
        audio = r.listen(source, timeout=5)

    # save the audio data to a file

    play("stopped-listening.mp3")

    print("Got it! Now to recognize it...")
    return audio


def recognize_audio(audio):
    try:
        # recognize speech using Google Speech Recognition
        with contextlib.redirect_stdout(io.StringIO()):
            value = r.recognize_google(audio)
        return value
    except sr.UnknownValueError as e:
        print("Oops! Didn't catch that")
        raise Exception("incomprehensible") from e
    except sr.RequestError as e:
        print(
            "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        raise Exception("bad API") from e
    finally:
        # delete the audio file
        # os.remove(filename)
        pass


def recognize():
    while 1:
        try:
            print('attempting to record')
            audio = record()
            save_audio(audio)
            print('recording succeeded')
        except:
            print('recording failed')
            continue
        try:
            print('attempting to recognize')
            text = recognize_audio(audio)
            print('audio recognition succeeded')
            break
        except:
            print('audio recognition failed')
            continue
    print("complete!")
    
    return text


if __name__ == "__main__":
    # adjust the noise once at the beginning of the session
    print("A moment of silence, please...")
    adjust_noise()

    # start the recognition loop
    text = recognize()

    print("You said: {}".format(text))
