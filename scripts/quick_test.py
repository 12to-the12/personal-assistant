# the necessity of this segment needs to be evaluated
from quick_parse import quick_parse
from example_instructions import example_instructions
from instruction_formation import instruction_to_command
import time
print(len(example_instructions))
misses = 0
hits = 0
for instruction in example_instructions:
    print()
    print(instruction)
    start = time.time()
    result = instruction_to_command(instruction)
    end = time.time()
    
    
    if end-start > 0.05:
        print(f"{(end-start):.2f} ms")
        hits += 1
    else:
        print(f"$ {result}")
        misses +=1
print()
print(hits)
print(misses)