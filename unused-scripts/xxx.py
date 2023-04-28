from elevenlabs import voices
import toml
from dotenv import load_dotenv
import os
# Open the TOML configuration file and load its contents
with open('config.toml') as f:
    config = toml.load(f)
dotenv_path = config["dotenv_path"]


load_dotenv(dotenv_path)
api_key = os.getenv("ElevenLabs_shiva")


from elevenlabs import set_api_key

set_api_key(api_key)

from elevenlabs.api import Voices
voices = Voices.from_api()
print(voices[0])
print(voices)