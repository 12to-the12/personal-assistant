#!/home/logan/software-development/projects/ai/personal-assistant/venv/bin/python

# entrypoint for one off requests to an ai model

from scripts.query import query_chat
import sys
from scripts.postprocessing import run_python


from rich.console import Console
console = Console(width=50)

from scripts.config import role

# Read the command-line input as a single item
query = ' '.join(sys.argv[1:])

print(f"{query}")
messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": query}
    ]


# print(messages)
response = query_chat(messages=messages)
# print("________________________________________-")

# console.print(f"[[bold red]response[/]]\n{response}")
print("________________________________________-")
# print(response)
response = run_python(response)
from scripts.voice_synth import say
console.print(f"[[bold red]response[/]]\n{response}")
print("________________________________________-")

say(text=response)
console.print(f"[[bold red]response[/]]\n{response}")

# print(response)
