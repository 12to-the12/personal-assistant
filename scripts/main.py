print("startup")
from spin_off import spin_off
from recognition import adjust_noise, record, recognize, recognize_audio
from instruction_formation import instruction_to_command
from commentary import give_commentary
# from say import say
from voice_synth import say
import time
import os
# from play import play
import signal
# startmp3 = play("start.mp3", asyncronous=True)
input_lock = False


def command_validator(command):  # returns pass
    project_types = ["python", "rust", "java",
                     "website", "cpp", "bash", "assembly"]
    command = command.split()
    if len(command) != 3:
        # print(f"a proper command should have three arguments, not {len(command)}")
        say("Sorry, I had some trouble knowing what you need, please specify a project language and name")
        return False
    if command[0] != "new-project":
        # print(f"a proper command should begin with new-project followed by a space, not {command[0]}")
        say("Sorry, I had some trouble knowing what you need, please specify a project language and name")
        return False
    if command[1] not in project_types:
        # print(f"a proper command should use a valid project type, not {command[1]}")
        message = f"Sorry, I'm not sure how to initialize {command[1]} projects, I've only been taught how to work with the following, "
        message += ", ".join(project_types)
        say(message)
        return False
    return True


# Write the server PID to a text file
pid_file = "var/assistant.pid"
with open(pid_file, 'w') as f:
    f.write(str(os.getpid()))

# Print the server PID for reference
print("Server PID:", os.getpid())

# Define a signal handler function to receive the signal
def signal_handler(signum, frame):
    global input_lock
    if input_lock: return None
    input_lock = True
    while 1:
        try: record()
        except:
            input_lock = False
            return None
        text = recognize_audio()
        # text = recognize()
        print(f"you said: {text}")
        # print("how do I put this into words...")
        command = instruction_to_command(text)
        print(f"command: {command}")
        if command_validator(command):
            os.system(command)
            give_commentary(command)
            break
        else:
            print('invalid command')
            pass
    
    input_lock = False


signal.signal(signal.SIGUSR1, signal_handler)


print("starting loop")
while 1:
    # signal.pause()
    
    if not input_lock:
        print("adjusting for noise...")
        adjust_noise()
    time.sleep(10)