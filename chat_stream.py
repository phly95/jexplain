import openai

openai.api_key = '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'

async def chat_stream(prompto):
  for chunk in openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature = 0.0,
    messages=[{
        "role": "user",
        "content": prompto
    }],
    stream=True,
):
    content = chunk["choices"][0].get("delta", {}).get("content")
    if content is not None:
        print(content, end='')

        