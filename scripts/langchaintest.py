# not utilized yet, self explanatory

print("importing...")
from dotenv import load_dotenv
import os
os.system("clear")
# import openai
from config import config
print("setting up...")
dotenv_path = config["dotenv_path"]
load_dotenv(dotenv_path)
# openai.api_key = os.getenv("OPENAI_API_KEY")
# os.environ["SERPAPI_API_KEY"]





import os
from collections import deque
from typing import Dict, List, Optional, Any

from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import BaseLLM
from langchain.vectorstores.base import VectorStore
from pydantic import BaseModel, Field
from langchain.chains.base import Chain
from langchain.experimental import BabyAGI


from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore


# Define your embedding model
embeddings_model = OpenAIEmbeddings()
# Initialize the vectorstore as empty
import faiss

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})


OBJECTIVE = "Write a weather report for SF today"

llm = OpenAI(temperature=0)

# Logging of LLMChains
verbose = False
# If None, will keep on going forever
max_iterations: Optional[int] = 3
baby_agi = BabyAGI.from_llm(
    llm=llm, vectorstore=vectorstore, verbose=verbose, max_iterations=max_iterations
)

baby_agi({"objective": OBJECTIVE})


