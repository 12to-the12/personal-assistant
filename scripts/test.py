from query import query
import time
import toml
with open('config.toml') as f:
    config = toml.load(f)

def command_validator(command):  # returns pass
    project_types = ["python", "rust", "java",
                     "website", "cpp", "bash", "assembly"]
    command = command.split()
    if len(command) != 3:
        print(f"a proper command should have three arguments, not {len(command)}")
        return False
    if command[0] != "new-project":
        print(f"a proper command should begin with new-project followed by a space, not {command[0]}")
        return False
    if command[1] not in project_types:
        print(f"a proper command should use a valid project type, not {command[1]}")
        return False
    return True

def log(msg, log_file='efficacy.txt'):
    with open(log_file, 'a') as f:
        f.write(msg + '\n')

if __name__ == "__main__":
    # sentence = "set up a C plus plus project file for me, I going to learn how to write command line utilities"
    sentence = "I'm learning python, set up a new repository for me"
    instruction = {
        "role": "instruction", "content": sentence}
    rounds = config["rounds"]
    correct_count = 0
    start = time.time()
    for round in range(rounds):
        speech, command = query(instruction)
        # print(speech)
        # print(command)
        if command_validator(command):
            correct_count += 1
            print('valid')
        else:
            print('invalid')
        print()
    end = time.time()
    time_taken = end-start
    print(f"{correct_count/rounds*100}% correct")
    log(f"{correct_count/rounds*100}% correct with \t{config['model']} @ {rounds} rounds, temp: {config['temperature']}  \t{time_taken/rounds:.2f} seconds average latency")
