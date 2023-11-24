# responsbile for actually making the openai api call
# from dotenv import load_dotenv
# import dotenv
import os
import openai
from pathlib import Path
from scripts.config import config



# logic for configuring the queries based on the config file
query_type = config["query_type"]
chat_model = config["chat_model"]
completion_model = config["completion_model"]



# finding the enviroment variables

# dotenv_path = config["dotenv_path"]
# load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

# creates a query chat for the newer openai models
def query_chat(messages=None, model=chat_model):
    
    assert messages != None, "messages cannot be an empty field"
    """
    see https://platform.openai.com/docs/guides/text-generation/chat-completions-api
    messages is a list of dictionaries, each being a message
    first a system, then a dialogue

      messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
    ]
    """
    print(f'posting chat query with {chat_model}')
    # print(model)
    # print(messages)

    client = openai.OpenAI()
    # response = openai.ChatCompletion.create(
    #     model=model,
    #     messages=messages
    # )
    completion = client.chat.completions.create(
      model=model,
      messages=messages
    )
    print('received')

    # response = response['choices'][0]['message']['content']
    response = completion.choices[0].message.content
    # print(completion)
    # print()
    # print(response)
    # quit()
    return response

