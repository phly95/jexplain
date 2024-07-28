import pyautogui
import time

def no_copy():
    pass

def ctrl_c_copy():
    pyautogui.hotkey('ctrl', 'c')

def c_copy():
    pyautogui.hotkey('c')

def custom_copy():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write("cs6767")
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)

# The custom copy is meant to be used with jpdb.io to copy the current sentence using a bookmarklet.
# It can be used with Firefox (not Chrome)

# Bookmark name: "copy sentence", Keyword: "cs6767", URL: "javascript:(function(){var e=document.querySelector("div.sentence");function t(e){let n="";for(const r of e.childNodes)r.nodeType===Node.TEXT_NODE?n+=r.textContent:r.tagName!==%22RT%22&&(n+=t(r));return%20n}navigator.clipboard.writeText(t(e)).then(()=%3E{console.log(%22Sentence%20copied!%22)},()=%3E{console.error(%22Copy%20failed%22)})})();"


copy_modes = [
    {"name": "No Copy", "function": no_copy},
    {"name": "Ctrl+C Copy", "function": ctrl_c_copy},
    {"name": "C Copy", "function": c_copy},
    {"name": "Custom Copy", "function": custom_copy}
]