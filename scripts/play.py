# import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# from pygame import mixer
# import pygame

# def pygame_play():
#     mixer.init()
#     mixer.music.load("audio.mp3")
#     mixer.music.play()
    

#     import time
#     while mixer.music.get_busy():  # wait for music to finish playing
#         time.sleep(0.2)
#     mixer.quit()

import pyglet
from scripts.spin_off import spin_off

# def on_player_eos():
#         pyglet.app.exit()
def play_audio_file(audio_file):
    sound = pyglet.media.load(audio_file, streaming=False)
    sound.play()
    
    # audio_file = pyglet.media.load(audio_file)
    # player = pyglet.media.Player()
    # player.queue(audio_file)
    # player.play()
    # pyglet.app.run()
    # pyglet.app.exit()

def play(audio_file, asyncronous=True):
    if asyncronous:
        process = spin_off(play_audio_file(audio_file))
        return process
    else:
        play_audio_file(audio_file)
        return None


if __name__ == "__main__":
    p = play('speech_synthesis.mp3', asyncronous=True)
    # p.join()
    import time
    time.sleep(3)
    

# import pyglet

# def play_audio(filename):
#     print('here')
#     player = pyglet.media.Player()
#     source = pyglet.media.load(filename)
#     player.queue(source)
#     print('there')
#     player.play()
#     print('everywhere')

# if __name__ == '__main__':
#     print('start')
#     filename = 'listening.mp3'
#     play_audio(filename)
#     print('back')
#     pyglet.app.run()
#     print('end')

