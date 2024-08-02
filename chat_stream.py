import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# client = OpenAI(api_key=os.environ.get("TOGETHER_API_KEY"), base_url="http://localhost:1234/v1")

async def chat_stream(prompto, model_set="gpt-4o-mini", temperature_set=0.0):
  totalstring = ""
  for chunk in client.chat.completions.create(model=model_set,
  temperature = temperature_set,
  messages=[{
      "role": "user",
      "content": prompto
  }],
  stream=True):
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end='', flush=True)
        totalstring +=content
  return totalstring