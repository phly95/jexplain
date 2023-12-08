from jp_process import jp_process, chat_with, kj_process, tr_process
from win_focus import set_title, winfocus, clear_screen, clear_input_buffer
import keyboard
import pyautogui
import time

set_title("jexplain_window")
print("Ready for scanning")
while True:
        time.sleep(0.05)
        if keyboard.is_pressed('ctrl+win+z'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('z'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                clear_screen()
                #print("Engaged")
                pyautogui.hotkey('ctrl', 'c')
                winfocus("jexplain_window")
                jp_process()
                print("\n***\n", end="")
        elif keyboard.is_pressed('ctrl+win+a'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('a'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                clear_input_buffer()
                chat_with(input("\nAsk a question: "))
                print("\n***\n", end="")
        elif keyboard.is_pressed('ctrl+win+tab'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('tab'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                # pyautogui.hotkey('ctrl', 'c')
                tr_process()
                print("\n***\n", end="")
        elif keyboard.is_pressed('ctrl+win+k'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('k'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                pyautogui.hotkey('ctrl', 'c')
                kj_process()
                print("\n***\n", end="")
