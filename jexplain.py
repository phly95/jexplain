import os
import json
import time
import pyperclip
import pyautogui
import keyboard
import subprocess
import threading

from copy_modes import copy_modes
from jp_process import jp_process, jp_process_lite, chat_with, kj_process, tr_process, tr_agressive, mnemonic_process, speak
from win_focus import set_title, winfocus, clear_screen, clear_input_buffer

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(script_dir, 'config')
os.makedirs(config_dir, exist_ok=True)

# Path to the file storing the current copy mode
copy_mode_file = os.path.join(config_dir, 'current_copy_mode.json')

# Load the current copy mode
def load_copy_mode():
    if os.path.exists(copy_mode_file):
        with open(copy_mode_file, 'r') as f:
            return json.load(f)['mode']
    return 0  # Default to no_copy

# Save the current copy mode
def save_copy_mode(mode):
    with open(copy_mode_file, 'w') as f:
        json.dump({'mode': mode}, f)

# Initialize the current copy mode
current_copy_mode = load_copy_mode()

set_title("jexplain_window")
print("Ready for scanning")

def monitor_clipboard():
    previous_clipboard_content = pyperclip.paste()
    identifier = "[MPV]"
    while True:
        time.sleep(0.05)  # Adjust the sleep interval as needed
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != previous_clipboard_content:
            if current_clipboard_content.startswith(identifier):
                # Remove the identifier
                processed_content = current_clipboard_content[len(identifier):].strip()
                previous_clipboard_content = current_clipboard_content
                pyperclip.copy(processed_content)

                # Trigger Ctrl+Win+Z action
                clear_screen()
                copy_modes[current_copy_mode]['function']()
                # winfocus("jexplain_window")
                jp_process_lite()
                print("\n***\n", end="")

# Start clipboard monitoring thread
clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
clipboard_thread.start()

while True:
    time.sleep(0.05)
    if keyboard.is_pressed('ctrl+win+z'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('\\'):
            pass
        clear_screen()

        copy_modes[current_copy_mode]['function']()  # Execute the current copy mode

        winfocus("jexplain_window")
        jp_process_lite()
        print("\n***\n", end="")
    elif keyboard.is_pressed('ctrl+win+-'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('-'):
            pass
        tr_agressive()
        print("\n***\n", end="")
    elif keyboard.is_pressed('ctrl+win+x'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('x'):
            pass
        copy_modes[current_copy_mode]['function']()
        speak('ja-JP-ShioriNeural')
        print("***\n", end="")
    elif keyboard.is_pressed('ctrl+win+f12'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('f12'):
            pass
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'c')
        speak('en-US-AvaNeural')
        print("***\n", end="")
    elif keyboard.is_pressed('ctrl+win+a'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('a'):
            pass
        clear_input_buffer()
        chat_with(input("\nAsk a question: "))
        print("\n***\n", end="")
    elif keyboard.is_pressed('ctrl+win+tab'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('tab'):
            pass
        tr_process()
        print("\n***\n", end="")
    elif keyboard.is_pressed('ctrl+win+k'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('k'):
            pass
        kj_process()
        print("\n***\n", end="")
    elif keyboard.is_pressed('ctrl+win+]'):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed(']'):
            pass
        clear_screen()
        pyautogui.hotkey('ctrl', 'c')
        winfocus("jexplain_window")
        mnemonic = mnemonic_process()
        pyperclip.copy(mnemonic)
        print("\n***\n", end="")
    elif keyboard.is_pressed('ctrl+win+['):
        while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('['):
            pass
        current_copy_mode = (current_copy_mode + 1) % len(copy_modes)
        save_copy_mode(current_copy_mode)
        print(f"Copy mode changed to: {copy_modes[current_copy_mode]['name']}")