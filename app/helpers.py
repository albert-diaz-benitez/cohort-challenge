from IPython.display import display, Markdown
from openai import OpenAI
def get_response(client: OpenAI, messages: str, model: str = "gpt-3.5-turbo") -> str:
    return client.chat.completions.create(
        model=model,
        messages=messages
    )

def system_prompt(message: str) -> dict:
    return {"role": "system", "content": message}

def assistant_prompt(message: str) -> dict:
    return {"role": "assistant", "content": message}

def user_prompt(message: str) -> dict:
    return {"role": "user", "content": message}

def pretty_print(message: str) -> str:
    display(Markdown(message.choices[0].message.content))