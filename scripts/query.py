from dotenv import load_dotenv
import dotenv
import os
import openai
from pathlib import Path


import toml
# Open the TOML configuration file and load its contents
with open('config.toml') as f:
    config = toml.load(f)

dotenv_path = config["dotenv_path"]
load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_APIKEY")


messages = [
    {"role": "system",    "content": "the assistant is witty, helpful, and knowledgeable"},
    {"role": "system",    "content": "available project types: python, rust, java, website, cpp, bash, assembly"},
    {"role": "user",      "content": "create a new python project about learning python"},
    {"role": "assistant",
        "content": "alright, creating the project $new-project python learning-python"},
    {"role": "user",      "content": "computer, make a new project. Name something like WASM fun, it's a rust project"},
    {"role": "assistant", "content": "on it, fun with W A S M coming right up $new-project rust fun-with-WASM"},
    {"role": "user",      "content": "hey, system assistant, build me a new java project file, I want it to be called java beans"},
    {"role": "assistant",
        "content": "you gotcha! one java project on it's way $new-project java java-beans"},
    {"role": "user",      "content": "assistant, I want to learn C++, open a new project file for that."},
    {"role": "assistant", "content": "Good luck to ya, C plus plus can be pretty daunting $new-project cpp learning-cpp"},
    {"role": "user", "content": "make me a new website about cars"},
    {"role": "assistant",
        "content": "Getting into cars are we? $new-project website all-about-cars"},
    {"role": "user", "content": "I want a python project set up for me. I'm gonna build a pacm-man clone."},
    {"role": "assistant",      "content": "I love pac man! $new-project python pac-man"},
    {"role": "user", "content": "hey computer, set up a java program for me, I want to learn how to mod Minecraft"},
    {"role": "assistant",
        "content": "Man,  that sounds like a good time $new-project java modding-minecraft"},
    # {"role": "user", "content": "set up a C plus plus project file for me, I going to learn how to write command line utilities"}

]

base_prompt = \
"""the assistant is witty, helpful, and knowledgeable
valid values for project_type: python, rust, java, website, cpp, bash, assembly

the new-project command will not work with other project types
the project_type value for c plus plus projects is written cpp

response format: <witty reply>$new-project <project_type> <project-name>

tailwind is a website tool, tailwind projects are project_type: website
wasm is used with rust, wasm projects are project_type: rust
machine learning projects are project_type: python



valid response examples:
instruction: create a new python project about learning python
response: alright, creating the project $new-project python learning-python
instruction: computer, make a new project. Name something like WASM fun, it's a rust project
response: on it, fun with W A S M coming right up $new-project rust fun-with-WASM
instruction: hey, system assistant, build me a new java project file, I want it to be called java beans
response: you gotcha! one java project on it's way $new-project java java-beans
instruction: assistant, I want to learn C++, open a new project file for that.
response: Good luck to ya, C plus plus can be pretty daunting $new-project cpp learning-cpp
instruction: make me a new website about cars
response: Getting into automotive stuff are we? $new-project website all-about-cars
instruction: I want a python project set up for me. I'm gonna build a pac-man clone.
response: I love pac man! $new-project python pac-man
instruction: hey computer, set up a java program for me, I want to learn how to mod Minecraft
response: Man,  that sounds like a good time $new-project java modding-minecraft
instruction: I want to make a new website about talking animals
response: Sound like a good idea, one website being made as we speak! $new-project website talking-animals
instruction: I'm learning python, set up a new repository for me
response: On it, one project folder coming right up! $new-project python first-steps-with-python
instruction: can you set up a project for me? I have a cool idea for a assembly project
response: You betcha. Good luck with assembly, it can be difficult $new-project assembly the-coolest-idea
instruction: Make me a new python project for interfacing with blender
response: Interfacing with Blender? And to think it was already so cool $new-project python python-and-blender
instruction: I'm curious abouut Java. please make me a Java project.
response: Java project. Here you go $new-project java baby-steps-with-java
"""


def query(instruction):
    
    messages.append(instruction)

    # print(messages)
    if config["model"]=="gpt-3.5-turbo" or config["model"]=="gpt-4":
        response = openai.ChatCompletion.create(
            model=config["model"],
            messages=messages,
            temperature=config["temperature"],
            max_tokens=config["max_tokens"]
        )
        # print(response)
        message = response.choices[0].message.content
    else:
        # prompt = ""
        # for message in messages:
        #   
        global prompt  
        prompt = base_prompt + instruction["role"]+": "+instruction["content"]+'\n'+"response: "
        # print("prompt: __________")
        # print(prompt)
        # print("__________")
        response = openai.Completion.create(
            engine=config["model"],
            prompt=prompt,
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
            stop="\n"
        )
        # print(response)
        
        message = response.choices[0].text
    
        print(message)
        try: message = message.split(':')[1]
        except: pass
    try:
        speech, command = message.split('$')
    except:
        speech,  command = message, ""
    return [speech, command]



if __name__ == "__main__":
    instruction = {
        "role": "user", "content": "set up a c plus plus project file for me, I am going to learn how to write command line utilities"}
    speech, command = query(instruction)
    print()
    print(speech)
    print(command)
