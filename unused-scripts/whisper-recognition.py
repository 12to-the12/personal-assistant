import whisper
from time import perf_counter


def log(msg, log_file='whisper-log.txt'):
    with open("logs/"+log_file, 'a') as f:
        f.write(msg + '\n')
    print(msg)

def recognize(audio_file):
    
    start = perf_counter()
    result = model.transcribe(audio_file)
    end = perf_counter()
    log(f"transcription: {end-start:.2f}s")
    log(result["text"])       
    # log(f"total: {c-a:.2f}s")
    
# tiny.en, small.en, base.en
if __name__ == "__main__":
    model = "tiny.en"
    log(f"__________ {model} __________")
    print(model)
    start = perf_counter()
    model = whisper.load_model(model)
    end = perf_counter()
    log(f"model load: {end-start:.2f}s")


    rounds = 10
    for round in range(rounds):
        recognize("sample.mp3")
    log("")


# import speech_recognition as sr
# from time import sleep
# import keyboard # pip install keyboard

# go = 1

# def quit():
#     global go
#     print("q pressed, exiting...")
#     go = 0

# keyboard.on_press_key("q", lambda _:quit()) # press q to quit

# r = sr.Recognizer()
# mic = sr.Microphone()
# print(sr.Microphone.list_microphone_names())

# mic = sr.Microphone(device_index=1)


# while go:
#     try:
#         sleep(0.01)
#         with mic as source:
#             audio = r.listen(source)
#             with open('temp.mp3', "wb") as f:
#                 f.write(audio.get_wav_data())
#             print(model.transcribe('temp.mp3'))
#             # print(r.recognize_google(audio))
#     except:
#         pass
    