
import subprocess
# import pyglet
from scripts.spin_off import spin_off
# this segment plays audio files
# it is supposed to keep everything in the audio-files directory

def play_audio_file(audio_file):
    print(audio_file)
    print("playing sound")
    process = subprocess.Popen(['mpv','--no-terminal', audio_file])


def play(audio_file):
    play_audio_file(audio_file)



if __name__ == "__main__":

    p = play('speech_synthesis.mp3')
    # p.join()
    import time
    time.sleep(3)
    
