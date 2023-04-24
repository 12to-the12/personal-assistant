from play import play
# startmp3 = play("start.mp3", asyncronous=True)
print("startup")
import toml
from voice_synth import synth
import json
import openai
import os
import time
from query import query
from recognition import adjust_noise, record, recognize
from spin_off import spin_off

with open('config.toml') as f:
    config = toml.load(f)













# with open('ambient.txt', 'r') as f:
#     ambient = int(f.readline().strip())

print("adjusting for noise...")
adjust_noise()

# startmp3.join()
print("I'll wait here...")
text = recognize()

print(f"you said: {text}")
print("how do I put this into words...")
start_time = time.time()
text = {"role": "user", "content": text}
response = query(text)
end_time = time.time()
flavor, command = response
print(f"speech: {flavor}")
print(f"command: {command}")


def log(msg, log_file='log.txt'):
    with open(log_file, 'a') as f:
        f.write(msg + '\n')
    # print(msg)


# def clear_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')
def command_validator(command):  # returns pass
    project_types = ["python", "rust", "java",
                     "website", "cpp", "bash", "assembly"]
    command = command.split()
    if len(command) != 3:
        # print(f"a proper command should have three arguments, not {len(command)}")
        return False
    if command[0] != "new-project":
        # print(f"a proper command should begin with new-project followed by a space, not {command[0]}")
        return False
    if command[1] not in project_types:
        # print(f"a proper command should use a valid project type, not {command[1]}")
        return False
    return True
print("running command...")
if command_validator(command):
    os.system(command)
else:
    print('invalid command')

log("__________ entry __________")
log(f"instruction: {text}")
log(flavor)
log(command)
# print(f"model: {config["model"]}")
# log(f"Tokens: \t{response.usage.total_tokens}")
log(f"openai api call:   \t{end_time - start_time:.2f} seconds")
log("")

print(f"wow, that took: {end_time - start_time:.2f} seconds\n")
print("how do I say this...")
spin_off( synth(flavor) )

# play("speech_synthesis.mp3")
time.sleep(3)