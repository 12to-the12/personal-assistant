from dotenv import load_dotenv
import dotenv
import os
from scripts.query import query_completion
from pathlib import Path



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


header = """valid values for project_type: python, rust, java, website, cpp, bash, assembly
THESE ARE THE ONLY VALID PROJECT TYPES

the project_type value for c plus plus projects is "cpp"
response format: new-project <project_type> <project-name>

valid response examples:
[instruction]: create a new python project about learning python
[response]:new-project python learning-python
[instruction]: computer, make a new project. Name something like WASM fun, it's a rust project
[response]:new-project rust fun-with-WASM
[instruction]: hey, system assistant, build me a new java project file, I want it to be called java beans
[response]:new-project java java-beans
[instruction]: assistant, I want to learn c plus plus, open a new project file for that.
[response]:new-project cpp learning-cpp
[instruction]: make me a new website about cars
[response]:new-project website all-about-cars
[instruction]: I want a python project set up for me. I'm gonna build a pac-man clone.
[response]:new-project python pac-man
[instruction]: hey computer, set up a java program for me, I want to learn how to mod Minecraft
[response]:new-project java modding-minecraft
[instruction]: I want to make a new website about talking animals
[response]:new-project website talking-animals
[instruction]: I'm learning python, set up a new repository for me
[response]:new-project python first-steps-with-python
[instruction]: can you set up a project for me? I have a cool idea for a assembly project
[response]:new-project assembly the-coolest-idea
[instruction]: Make me a new python project for interfacing with blender
[response]:new-project python python-and-blender
[instruction]: I'm curious abouut Java. please make me a Java project.
[response]:new-project java baby-steps-with-java
[instruction]: computer, I want to make an intepreter in python
[response]:new-project python intepreter
[instruction]: make me a new c plus plus repo for game dev
[response]:new-project cpp game-dev
[instruction]: I need to write some game logic for a minecraft mod I'm making, new java project file
[response]:new-project java minecraft-game-logic
[instruction]: new emulator python project
[response]:new-project python emulator
[instruction]: make a new arduino rust project file
[response]:new-project rust arduino
[instruction]: I want to mess around with tailwind, new project file
[response]:new-project website fun-with-tailwind
[instruction]: let's make stuff run fast with w a s m
[response]:new-project rust fast-with-wasm
[instruction]: make a new assembly project called automate
[response]:new-project assembly automate"""


def instruction_to_command(instruction):
    global header
    prompt = header+"\n[instruction]: "+instruction+"\n"+"[response]:"
    # print(prompt, end="")   
    response = query_completion(prompt)
    response = response.lower()
    return response






if __name__ == "__main__":
    instruction = "set up a c plus plus project file for me, I am going to learn how to write command line utilities"
    response = instruction_to_command(instruction)
    print(f'<and then>{response}<cool right?>')
