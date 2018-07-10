import pyautogui
import time


def wait_maximize_finish():
    time.sleep(0.5)


def maximize_current_window():
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('x')
    wait_maximize_finish()
