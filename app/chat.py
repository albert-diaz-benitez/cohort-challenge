import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from app.helpers import get_response, user_prompt, pretty_print, system_prompt, assistant_prompt

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()
YOUR_PROMPT = "What is the difference between LangChain and LlamaIndex?"

# Testing helper functions
messages = [user_prompt(YOUR_PROMPT)]

chatgpt_response = get_response(client, messages)

pretty_print(chatgpt_response)

list_of_prompts = [
    system_prompt("You are irate and extremely hungry."),
    user_prompt("Do you prefer crushed ice or cubed ice?")
]
list_of_prompts[0] = system_prompt("You are joyful and having an awesome day!")

joyful_response = get_response(client, list_of_prompts)
pretty_print(joyful_response)

# few-shot prompting
list_of_prompts = [
    user_prompt("Something that is 'stimple' is said to be good, well functioning, and high quality. An example of a sentence that uses the word 'stimple' is:"),
    assistant_prompt("'Boy, that there is a stimple drill'."),
    user_prompt("A 'falbean' is a tool used to fasten, tighten, or otherwise is a thing that rotates/spins. An example of a sentence that uses the words 'stimple' and 'falbean' is:")
]

stimple_response = get_response(client, list_of_prompts)
pretty_print(stimple_response)

# chain of thought prompting
reasoning_problem = """
Billy wants to get home from San Fran. before 7PM EDT.

It's currently 1PM local time.

Billy can either fly (3hrs), and then take a bus (2hrs), or Billy can take the teleporter (0hrs) and then a bus (1hrs).

Does it matter which travel option Billy selects?
"""

list_of_prompts = [
    user_prompt(reasoning_problem)
]

reasoning_response = get_response(client, list_of_prompts)
pretty_print(reasoning_response)