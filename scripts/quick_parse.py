# this segment is designed to offload simple pre processing parsing tasks from the gpt api call

valid_project_types = [ 'python', 'rust', 'java', 'website', 'cpp', 'bash', 'assembly' ]

project_triggers = ['project', 'program', 'repo', 'repository', 'in']

multi_mappings = {
    'c plus plus': 'cpp',
    'w a s m': 'wasm'
}

mappings = {
    'tailwind': 'website',
    'wasm': 'rust'
}
name_triggers = ['called', 'titled', 'named']


# multi_word_tokens = [ 'c plus plus', 'w a s m']


def quick_parse(text):
    text = text.lower()
    text = text.replace(',', ' ')
    text = text.replace('new', '')
    project_trigger = None
    name_trigger = None
    # print(text)
    
    for token in multi_mappings.keys():
        if token in text: text = text.replace(token, multi_mappings[token])
    words = text.split()
    # print(words)

    for position, word in enumerate(words):
        # print(word)
        if word in mappings.keys(): words[position] = mappings[word]

    # print(' '.join(words))
    for word in project_triggers:
        if word in words: project_trigger = word

    for word in name_triggers:
        if word in words: name_trigger = word

    # print('project_trigger: ',project_trigger)
    # print('name_trigger: ',name_trigger)
    project_type = None
    for ptype in valid_project_types:
        if ptype in words:
            project_type = ptype
    # if project_trigger != None:
    #     trigger_location = words.index(project_trigger)
    #     project_type_index = trigger_location - 1
    #     project_type = words[project_type_index]
    #     if project_type not in valid_project_types: raise Exception(f"difficulty parsing, {project_type} is not a valid project type")   
    if project_type == None:
        raise Exception("difficulty parsing, no 'project'")


    if name_trigger != None:
        # print()
        # print(line)
        trigger_location = words.index(name_trigger)
        project_name_index = trigger_location + 1
        project_name = '-'.join(  words[project_name_index:]  )    
    else:
        raise Exception("difficulty parsing")   
    
    # print(f"project type: {p[roject_type}\nproject name: {project_name}")
    return(f"new-project {project_type} {project_name}")








if __name__ == "__main__":

    xxx = \
"""[instruction]: create a new python project about learning python
[response]:new-project python learning-python
[instruction]: computer, make a new project. Name it something like WASM fun, it's a rust project
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
[instruction]: can you set up a project for me? I have a cool idea for an assembly project
[response]:new-project assembly the-coolest-idea
[instruction]: Make me a new python project for interfacing with blender
[response]:new-project python python-and-blender
[instruction]: I'm curious about Java. please make me a Java project.
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
    print('\n'*5)
    xxx = xxx.split('\n')
    # for x in xxx:print(x)


    for id, line in enumerate(xxx):
        if id%2==0:
            # print()

            # print(line[:15])
            line = line[15:]

            line = line.lower()
            line = line.replace(',', ' ')
            print(line)
            # try:
            #     print(f"$ {quick_parse(line)}")
            #     # print("pass")
            # except:
            #     print(f"couldn't parse ''{line}''")
            #     # print("fail")
    print('start')
    print()
    print(quick_parse("new rust repo about cloning"))