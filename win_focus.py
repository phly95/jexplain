import win32gui
import re
import win32console
import pyautogui
import os
import msvcrt

def winfocus(title):
    pyautogui.press("alt")
    w.find_window_wildcard(".*jexplain_window.*")
    w.set_foreground()

def set_title(title):
    win32console.SetConsoleTitle(title)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

import sys

def print_bottom(text):
    sys.stdout.write("\033[J") # Clear everything below the cursor
    sys.stdout.write("\033[999;1H") # Move cursor to the last line
    print(text, end="")

def clear_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


w = WindowMgr()