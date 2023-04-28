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


def query_completion(prompt):
    response = openai.Completion.create(
        engine=config["model"],
        prompt=prompt,
        temperature=config["temperature"],
        max_tokens=config["max_tokens"]
        # stop="\n"
    )
    # print(response)
    response = response.choices[0].text
    return response

if __name__ == "__main__":
    print( query_completion("Say hello") )