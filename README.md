A glorious swiss army knife of a project



[whisper-jax repo](https://github.com/sanchit-gandhi/whisper-jax)
[openai-whisper api reference](https://github.com/openai/whisper)
[elevenlabs api reference](https://github.com/elevenlabs/elevenlabs-python/blob/main/API.md)
[openai api reference](https://platform.openai.com/docs/api-reference/introduction)
[great free sound effects](https://www.zapsplat.com/sound-effect-category/alerts-and-prompts/page/9/)
[nice writeup on the signal package](https://medium.com/fintechexplained/advanced-python-how-to-use-signal-driven-programming-in-applications-84fcb722a369)
Road map:
1. streamline the cli usage, add some CLI arguments to the python script
2. look into color and animations
3. more commands, next up wwould be project review and project opening
4. add more metadata to project files
5. integrate with Obsidian



# Overview
The project runs the command 
```new-project```
with the arguments project_type and project_name

the script is not included, the instruction_formation controls how the command is generated
the implementation is very machine specific, so maybe ewrite your own



# Keep in Mind
make sure to activate the virtual enviroment with 
```source venv/bin/activate```
you can deactivate it with
```deactivate```

# Instructions


rename ".env-template to ".env"
fill in your openai api key in ".env"

run
```./build_venv```
in the project directory to automatically build the virtual enviroment


# Troubleshooting
on a mac run
```
brew install portaudio
pip install pyaudio
```
in the virtual enviroment to get pyaudio working
