# jexplain
Tool to quickly explain the usage of words in Japanese sentences by using Large Language models (Currently with Groq API using Llama 3 70b, formerly utilized ChatGPT).

This Readme is a basic description of the program's functions.

## Setup
Before running the program, you'll need to set up the following environment variables for API keys:

* **DEEPL_API_KEY:** Your API key for DeepL translation service.
* **GROQ_API_KEY:** Your API key for Groq language model service.
* **AZURE_SPEECH_API_KEY:** Your API key for Azure Speech service (optional, for text-to-speech functionality).

To run the program, simply execute the `jexplain.py` file with Python. 

## Global Keyboard Shortcuts:

* **Ctrl+Win+Z:** Explain the meaning of each word in the context of the sentence that is highlighted (autofocuses terminal window)
* **Ctrl+Win+A:** Ask a question to the AI
* **Ctrl+Win+Tab:** Translate the contents of the clipboard using DeepL
* **Ctrl+Win+K:** Explain the meaning of each Kanji in the highlighted word.
* **Ctrl+Win+\\:** Translate the highlighted text with DeepL, then explain each word. (depricated, since Ctrl+Win+Z already includes translation now)
* **Ctrl+Win+] / Ctrl+Win+[:** Generate a mnemonic sentence with the highlighted text.
* **Ctrl+Win+::** Speak the highlighted Japanese text.
* **Ctrl+Win+F12:** Speak the highlighted English text. 

## Functionality

* **Word Explanations:** The program uses the Groq language model API to provide context-specific definitions of Japanese words within sentences including furigana (furigana may contain inaccuracies) 
* **Kanji Breakdown:**  It can also explain the meaning of individual kanji characters within a word. 
* **Translation:**  DeepL API is used to translate Japanese text into English.
* **Text-to-Speech:**  With the Azure Speech service, you can hear the pronunciation of highlighted Japanese or English text. 
* **Mnemonic Generation:**  The program can create mnemonic sentences using highlighted text to aid in memorization for JPDB.io Kanji pages.
* **AI language model Interaction:**  You can directly ask questions to the Groq language model API for a more conversational experience. 

## Additional Notes:

*  Ensure you have the required Python libraries installed (deepl, groq, keyboard, pyautogui, pyperclip, win32gui, win32console, azure-cognitiveservices-speech).
* The program relies on keyboard shortcuts for activation.  
* It utilizes the clipboard for text input.  
* The terminal window is used for displaying outputs. 