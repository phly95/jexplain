import os
import configparser
from openai import OpenAI

# Read the configuration file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config', 'config.ini'))

# Get the API key from the configuration file or environment variable, with a fallback value
api_key_placeholder = config.get('openai', 'api_key')
if api_key_placeholder.startswith('${') and api_key_placeholder.endswith('}'):
    env_var_name = api_key_placeholder[2:-1]
    api_key = os.getenv(env_var_name, '1234')
else:
    api_key = api_key_placeholder

# Get the default model from the configuration file
default_model = config.get('openai', 'default_model')

# Get the base URL if it is provided, otherwise set it to None
base_url = config.get('openai', 'base_url', fallback=None)

# Initialize the OpenAI client
if base_url:
    client = OpenAI(api_key=api_key, base_url=base_url)
else:
    client = OpenAI(api_key=api_key)

async def chat_stream(prompto, model_set=default_model, temperature_set=0.0):
    totalstring = ""
    for chunk in client.chat.completions.create(model=model_set,
                                                temperature=temperature_set,
                                                messages=[{
                                                    "role": "user",
                                                    "content": prompto
                                                }],
                                                stream=True):
        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, end='', flush=True)
            totalstring += content
    return totalstring
