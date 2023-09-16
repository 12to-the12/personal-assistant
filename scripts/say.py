# not exactly sure what this is supposed to do, I guess say stuff from the cli?

from scripts.voice_synth import say
import sys


# Read the command-line input as a single item
# input = ' '.join(sys.argv[1:])
# say(input)

input = ""
for line in sys.stdin:
    input += line
print(input)
say(input)