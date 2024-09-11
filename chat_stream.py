# chat_stream.py

import os
import configparser
from itertools import cycle

# Read the configuration file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config', 'config.ini'))

if config.get('openai', 'api_type') == 'azure':
    from openai import AzureOpenAI as OpenAI
    api_type = 'azure'
elif config.get('openai', 'api_type') == 'google':
    import google.generativeai as genai
    api_type = 'google'
else:
    from openai import OpenAI
    api_type = 'openai'

# Get the API keys from the configuration file or environment variable, with a fallback value
api_keys = []
if config.has_option('openai', 'api_keys'):
    api_keys_placeholder = config.get('openai', 'api_keys').split(',')
    for key in api_keys_placeholder:
        if key.startswith('${') and key.endswith('}'):
            env_var_name = key[2:-1]
            api_key = os.getenv(env_var_name, '1234')
        else:
            api_key = key
        api_keys.append(api_key)
else:
    api_key_placeholder = config.get('openai', 'api_key')
    if api_key_placeholder.startswith('${') and api_key_placeholder.endswith('}'):
        env_var_name = api_key_placeholder[2:-1]
        api_key = os.getenv(env_var_name, '1234')
    else:
        api_key = api_key_placeholder
    api_keys.append(api_key)

# Get the default model from the configuration file
default_model = config.get('openai', 'default_model')

# Get optional parameters with fallbacks
base_url = config.get('openai', 'base_url', fallback=None)
api_version = config.get('openai', 'api_version', fallback=None)
azure_endpoint = config.get('openai', 'azure_endpoint', fallback=None)

# Initialize clients for each API key
clients = []
for api_key in api_keys:
    client_params = {"api_key": api_key}
    if base_url:
        client_params["base_url"] = base_url
    if api_version:
        client_params["api_version"] = api_version
    if azure_endpoint:
        client_params["azure_endpoint"] = azure_endpoint

    if api_type == 'google':
        genai.configure(api_key=api_key)
        clients.append(genai)
    else:
        clients.append(OpenAI(**client_params))

# Create a cycle iterator for the clients
client_cycle = cycle(clients)

if api_type == 'google':
    async def chat_stream(prompto, model_set=default_model, temperature_set=0.0):
        totalstring = ""

        # Define safety settings to block none for all categories
        safety_settings = {
            "HARM_CATEGORY_HARASSMENT": "block_none",
            "HARM_CATEGORY_HATE_SPEECH": "block_none",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "block_none",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "block_none",
        }

        # Get the next client from the cycle
        client = next(client_cycle)

        response = client.GenerativeModel(model_set).generate_content(
            prompto,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature_set
            ),
            safety_settings=safety_settings,
            stream=True
        )

        for chunk in response:
            if chunk.text:
                print(chunk.text, end='', flush=True)
                totalstring += chunk.text

        return totalstring
else:
    async def chat_stream(prompto, model_set=default_model, temperature_set=0.0):
        totalstring = ""

        # Get the next client from the cycle
        client = next(client_cycle)

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
