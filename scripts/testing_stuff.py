
# this file's purpose is to provide a quick way to verify all components are functioning as they are supposed to

from dotenv import load_dotenv
import dotenv
import os
import openai
from pathlib import Path
from config import config




if config["model"] == "gpt-3.5-turbo" or config["model"] == "gpt-4":
    config["chat"] = True
else:
    config["chat"] = False


dotenv_path = config["dotenv_path"]
load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")


# Initialize the completion endpoint
completion = openai.Completion()

def generate_response(prompt):
    # Set the model and parameters
    model = 'gpt-4'
    temperature = 0.8
    max_tokens = 50
    stop_sequence = '\n'

    # Generate an initial response using `openai.Completion.create()`
    response = completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop_sequence
    )

    # Stream the response by appending tokens to the prompt
    while not response['choices'][0]['text'].endswith(stop_sequence):
        prompt += response['choices'][0]['text']
        response = completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop_sequence
        )

    # Extract the final response from the streamed response
    final_response = prompt + response['choices'][0]['text'].rstrip(stop_sequence)
    return final_response

# Test the streaming response generation
prompt = "Q: What is the meaning of life?"
response = generate_response(prompt)
print(response)
