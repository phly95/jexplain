import pyperclip
from chat_stream import chat_stream
import asyncio


def jp_process():
    japanese_sentence = pyperclip.paste().replace('\n', '').replace('\r', '')
    bprompt = f"In this format \"- 言葉【ことば】: Context-specific English definition\" define each individual word (including particles) in the Japanese sentence in its original conjugation. Include the furigana, even if it's not needed (eg. \"おい【おい】: hey\").:\" 「{japanese_sentence}」 Your output should start with \"- \". #no-search"
    asyncio.run(chat_stream(bprompt))

def kj_process():
    kanji = pyperclip.paste().replace('\n', '').replace('\r', '')
    bprompt = f"What does each kanji in the word「{kanji}」 mean? #no-search"
    asyncio.run(chat_stream(bprompt))

def tr_process():
    japanese_sentence = pyperclip.paste().replace('\n', '').replace('\r', '')
    bprompt = f"Translate this to English:「{japanese_sentence}」"
    asyncio.run(chat_stream(bprompt))

def chat_with(question):
    asyncio.run(chat_stream(question))