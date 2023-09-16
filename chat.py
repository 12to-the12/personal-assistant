# an alternative entrypoint
# cli based

from scripts.query import query_chat
import sys
from rich.console import Console
console = Console(width=50)



# Read the command-line input as a single item
query = ' '.join(sys.argv[1:])


messages = [
        {"role": "system", "content": "The following is a conversation between an AI assistant and a user"},
        {"role": "user", "content": query}
    ]
print('here')
response = query_chat(messages=messages)

print(response)
# # console.print(f"[[bold red]reponse[/]]{response}")
