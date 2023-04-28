#!/usr/bin/env python



# import click
# from rich import print as rprint

import os
import subprocess
from query import query
from voice_synth import synth
from play import play
from recognition import recognize, adjust_noise


# import toml
# # Open the TOML configuration file and load its contents
# with open('config.toml') as f:
#     config = toml.load(f)

# user = 'user'
# gpt3 = 'ai'
# chat = f'the following is a conversation between a {user} and an omnipotent {gpt3}'


def repl():
    # global chat
    # print('\npress enter to quit\n')
    while 1:
        # print('\n\n',chat,'\n\n')


        # user_input = input('>> ')
        
        user_input = recognize()
        if user_input == None:
            print('.', end='')
            continue

        print(user_input)
        

        # chat += f'\n{user}: {user_input}\n{gpt3}: ' 
        try: reply = query(user_input)
        except Exception as ex:
            raise Exception(ex)
            break
        print('________________')
        print("(reply)")
        print(reply)
        if "```" in reply:
            code_block = reply.split("```",2)[1]
            type = code_block.split("\n")[0]
            code_block = "\n".join( code_block.split("\n")[1:]   )

            print('code:\n',code_block)
            
            if type == "python":
                print('\nrunning...\n\n')
                try: exec(code_block)
                except: print('error running')
                print('\n')

            if type == "bash":
                commands = code_block.split('\n')
                print("(executing shell script)")
                for command in commands:
                    arguments = command.split()
                    print(arguments)
                    subprocess.run(arguments, shell=True)

            continue
        print('\n>> ')
        # print(reply)

        # chat += reply

        try: synth(reply)
        except Exception as ex:
            raise Exception(ex)
            break

        
        
        try: play()
        except Exception as ex:
            raise Exception(ex)
            break

        


if __name__ == "__main__":
    os.system('clear')
    adjust_noise()
    try: repl()
    except Exception as ex:
            raise Exception(ex)


    print('\n<program ended>')
