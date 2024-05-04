from jp_process import jp_process, chat_with, kj_process, tr_process, mnemonic_process, speak#, screen_process
from win_focus import set_title, winfocus, clear_screen, clear_input_buffer
import keyboard
import pyautogui
import time
import pyperclip

set_title("jexplain_window")
print("Ready for scanning")
while True:
        time.sleep(0.05)
        if keyboard.is_pressed('ctrl+win+z'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('\\'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                clear_screen()
                #print("Engaged")
                pyautogui.hotkey('ctrl','c')# 'ctrl',
                # pyautogui.hotkey('ctrl','l')#
                # pyautogui.write("cs6565")  # Type "cs6565"
                # pyautogui.press('enter')  # Press Enter
                winfocus("jexplain_window")
                jp_process()
                print("\n***\n", end="")
        if keyboard.is_pressed('ctrl+win+\\'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('z'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                clear_screen()
                #print("Engaged")
                pyautogui.hotkey('ctrl','c')# 
                winfocus("jexplain_window")
                translation = tr_process()
                print("\n***\n", end="")
                pyperclip.copy(pyperclip.paste() + "\n" + translation)
                # print(pyperclip.paste())
                jp_process()
                print("\n***\n", end="")
        if keyboard.is_pressed('ctrl+win+]'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed(']'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                clear_screen()
                #print("Engaged")
                pyautogui.hotkey('ctrl','c')# 
                winfocus("jexplain_window")
                mnemonic = mnemonic_process(0)
                pyperclip.copy(mnemonic)
                #winfocus("jexplain_window")
                print("\n***\n", end="")
        if keyboard.is_pressed('ctrl+win+['):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('['): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                clear_screen()
                #print("Engaged")
                pyautogui.hotkey('ctrl','c')# 
                winfocus("jexplain_window")
                mnemonic = mnemonic_process(1)
                pyperclip.copy(mnemonic)
                #winfocus("jexplain_window")
                print("\n***\n", end="")
        if keyboard.is_pressed('ctrl+win+:'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed(':'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                # print("Speaking")
                time.sleep(0.1)
                pyautogui.hotkey('ctrl','c')# 
                # pyautogui.hotkey('ctrl','l')#
                # pyautogui.write("cs6565")  # Type "cs6565"
                # pyautogui.press('enter')  # Press Enter
                speak('ja-JP-ShioriNeural')
                print("***\n", end="")
        if keyboard.is_pressed('ctrl+win+f12'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('f12'): #wait until keys are released, so that ctrl+c can be pressed without interference
                        pass
                # print("Speaking")
                time.sleep(0.1)
                pyautogui.hotkey('ctrl','c')# 
                speak('en-US-AvaNeural')
                print("***\n", end="")
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
                # pyautogui.hotkey('ctrl', 'c')
                kj_process()
                print("\n***\n", end="")
        # elif keyboard.is_pressed('ctrl+win+c'):
        #         while keyboard.is_pressed('ctrl') or keyboard.is_pressed('win') or keyboard.is_pressed('c'): #wait until keys are released, so that ctrl+c can be pressed without interference
        #                 pass
        #         screen_process()
        #         print("\n***\n", end="")
