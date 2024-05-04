import pyperclip
from chat_stream import deepl, chat_stream_groq
import asyncio
import subprocess
import re
import azure.cognitiveservices.speech as speechsdk
import os

def jp_process():
    japanese_sentence = pyperclip.paste().replace('\n', '').replace('\r', '')
    bprompt = f"In plain text, first, translate the Japanese sentence. Then, in this format \"- 言葉【ことば】: Context-specific English definition\" define each individual word (including particles) in the Japanese sentence in its original conjugation. Include the furigana, even if it's not needed (eg. \"おい【おい】: hey\").:\" 「{japanese_sentence}」 Your output should start with \"Translation:\". Do not explain what you are about to do. After translation, you will write \"Breakdown:\" and bullet the list with hyphens \"- \""
    print("Sentence: " + japanese_sentence + "\n")
    asyncio.run(chat_stream_groq(bprompt))

def kj_process():
    kanji = pyperclip.paste().replace('\n', '').replace('\r', '')
    bprompt = f"What does each kanji in the word「{kanji}」 mean?"
    asyncio.run(chat_stream_groq(bprompt))

def mnemonic_process(temp):
    text = pyperclip.paste()
    # Split the text into lines
    lines = text.splitlines()

    # Find the index of the "Info" line
    info_index = lines.index('Info')

    # Join the lines before "Info" into a single string
    result = ', '.join(lines[:info_index])
    main_word = result

    # Find the "Composed of" line and join the following lines into a single string,
    # removing any non-ASCII characters and leading/trailing whitespace
    composed_index = info_index + 1
    while not lines[composed_index].startswith('Composed of'):
        composed_index += 1
    composed_parts = [part for part in (re.sub(r'[^\x00-\x7F]+', '', line.strip()) for line in lines[composed_index+1:]) if part]
    if result:
        result += ', '
    result += ', '.join(composed_parts)
    bprompt = f'Write a sentence using the following words: {result}. Each word listed should be bolded using markdown (surrounded by two asterisks "**"), except the main word, {main_word} should be surrounded by three asterisks, like so: "***{main_word}***".'
    mnemonic = chat_stream_groq(bprompt)
    return mnemonic

def tr_process():
    japanese_sentence = pyperclip.paste().replace('\n', '').replace('\r', '')
    bprompt = f"Translate this to English:「{japanese_sentence}」. Respond with only the translation without using quotation marks."
    translation = asyncio.run(deepl(japanese_sentence))
    return translation

def chat_with(question):
    asyncio.run(chat_stream_groq(question))

def speak(voice):
    japanese_sentence = pyperclip.paste().replace('\n', '').replace('\r', '')
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get("AZURE_SPEECH_API_KEY"), region="eastus")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name=voice#Shiori, Aoi

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_text_async(japanese_sentence).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(japanese_sentence))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())