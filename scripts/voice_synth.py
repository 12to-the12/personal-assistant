from elevenlabs import generate, play, stream, set_api_key
from dotenv import load_dotenv
import os
import toml

with open('config.toml') as f:
    config = toml.load(f)
dotenv_path = config["dotenv_path"]


# load_dotenv(dotenv_path)
# api_key = os.getenv("ELEVEN_API_KEY")


# set_api_key(api_key=api_key)


def synth_static(text):
    voice = config["voice"]
    audio = generate(
        text=text,#f"Hi! My name is {voice}, nice to meet you!",
        voice=voice
        # api_key=api_key
    )
    # file_path = "/dictation/speech_synthesis.mp3"
    # with open(file_path, 'wb') as file:
    #     file.write(audio)

    # return audio
    play(audio)


def say(text, voice="Rachel"):  # streaming
    audio_stream = generate(
        text=text,
        stream=True,
        voice=config["voice"]
    )

    stream(audio_stream)


if __name__ == "__main__":
    print('start...')
    say("Our Father, which art in heaven, Hallowed be thy Name. Give us this day our daily bread. And forgive us our trespasses, As we forgive them that trespass against us.")
    # play(audio)
