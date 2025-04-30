import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()
YOUR_PROMPT = "What is the difference between LangChain and LlamaIndex?"

client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role" : "user", "content" : YOUR_PROMPT}]
)