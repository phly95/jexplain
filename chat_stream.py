import deepl
from groq import Groq
import os

auth_key=os.environ.get("DEEPL_API_KEY")
translator = deepl.Translator(auth_key)
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

async def deepl(prompto):
   result = translator.translate_text(prompto, target_lang="EN-US")
   print(result.text, end='')
   return result.text

async def chat_stream_groq(prompto, model_set="llama3-70b-8192", temperature_set=0.0):
  totalstring = ""
  for chunk in groq_client.chat.completions.create(model=model_set,
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