#!/home/logan/software-development/projects/ai/personal-assistant/venv/bin/python
# directly invoked audio repl


# listen for audio ->
# transcribe audio to text ->
# make api call to gpt-4 ->
# text to speech with elevenlabs -->
# repeat

print("testing testing!")
from scripts.recognition import adjust_noise, record, recognize, recognize_audio
import time

from scripts.query import query_chat

from scripts.voice_synth import stream

import logging # for turning off output if it's not important enough
# see https://realpython.com/python-logging/
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")
logging.basicConfig(level=logging.DEBUG)

# clear = lambda : os.system("clear")



messages = []
print("starting loop")
while 1:
    print("adjusting for noise...")
    adjust_noise()
    transcript = recognize()
    print("you said")
    print(transcript)

    messages.append(transcript)
    response = query_chat(messages)
    print("agent said")
    print(response)

    print("converting to speech")
    stream(response)

