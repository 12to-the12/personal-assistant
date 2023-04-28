from dotenv import load_dotenv
import dotenv
import os
from query import query_completion
from pathlib import Path
from voice_synth import say
from spin_off import spin_off



# messages = [
#     {"role": "system",    "content": "the assistant is witty, helpful, and knowledgeable"},
#     {"role": "system",    "content": "available project types: python, rust, java, website, cpp, bash, assembly"},
#     {"role": "user",      "content": "create a new python project about learning python"},
#     {"role": "assistant",
#         "content": "alright, creating the project $new-project python learning-python"},
#     {"role": "user",      "content": "computer, make a new project. Name something like WASM fun, it's a rust project"},
#     {"role": "assistant", "content": "on it, fun with W A S M coming right up $new-project rust fun-with-WASM"},
#     {"role": "user",      "content": "hey, system assistant, build me a new java project file, I want it to be called java beans"},
#     {"role": "assistant",
#         "content": "you gotcha! one java project on it's way $new-project java java-beans"},
#     {"role": "user",      "content": "assistant, I want to learn C++, open a new project file for that."},
#     {"role": "assistant", "content": "Good luck to ya, C plus plus can be pretty daunting $new-project cpp learning-cpp"},
#     {"role": "user", "content": "make me a new website about cars"},
#     {"role": "assistant",
#         "content": "Getting into cars are we? $new-project website all-about-cars"},
#     {"role": "user", "content": "I want a python project set up for me. I'm gonna build a pacm-man clone."},
#     {"role": "assistant",      "content": "I love pac man! $new-project python pac-man"},
#     {"role": "user", "content": "hey computer, set up a java program for me, I want to learn how to mod Minecraft"},
#     {"role": "assistant",
#         "content": "Man,  that sounds like a good time $new-project java modding-minecraft"},
#     # {"role": "user", "content": "set up a C plus plus project file for me, I going to learn how to write command line utilities"}

# ]


# tailwind is a website tool, tailwind projects are project_type: website
# wasm is used with rust, wasm projects are project_type: rust
# machine learning projects are project_type: python
# responses have three parts, "new-project", the project_type, and the project_name


header = """
[instruction]: new-project python learning-python
[response]: Sure, I can help you with that. I created a new Python project for you with the name "learning-python".
[instruction]: new-project rust wasm-fun
[response]: Certainly! I created a new Rust project with the name "fun-with-WASM" as per your request.
[instruction]: new-project java java-beans
[response]: Sure, I created a new Java project for you with the name "java beans" as you requested.
[instruction]: new-project cpp learning-cplusplus
[response]: No problem, I created a new C++ project for you with the name "learning-cpp" to help you get started.
[instruction]: new-project website all-about-cars
[response]: Certainly, I created a new website project for you with the name "all-about-cars".
[instruction]: new-project python pac-man
[response]: Great idea! I created a new Python project for you with the name "pac-man" to help you build your clone.
[instruction]: new-project java modding-minecraft
[response]: Sounds interesting! I created a new Java project for you with the name "modding-minecraft" to help you get started.
[instruction]: new-project website talking-animals
[response]: Sure thing, I created a new website project for you with the name "talking-animals".
[instruction]: new-project python first-steps-with-python
[response]: Absolutely, I created a new Python project for you with the name "first-steps-with-python".
[instruction]: new-project assembly the-coolest-idea
[response]: Sure, I created a new Assembly project for you with the name "the-coolest-idea" to help you bring your idea to life.
[instruction]: new-project python python-and-blender
[response]: Sure thing! I created a new Python project for you with the name "python-and-blender" to help you interface with Blender.
[instruction]: new-project java baby-steps-with-java
[response]: Great, I created a new Java project for you with the name "baby-steps-with-java" to help you get started."""

@spin_off
def give_commentary(instruction):
    global header
    prompt = header+"\n[instruction]: "+instruction+"\n"+"[response]:"
    # print(prompt, end="")   
    response = query_completion(prompt)
    response = response.lower()
    say(response)
    # return response






if __name__ == "__main__":
    instruction = "set up a c plus plus project file for me, I am going to learn how to write command line utilities"
    response = give_commentary(instruction)
    print(f'<and then>{response}<cool right?>')
