import time

import pyautogui


def wait_window_maximize_finish():
    time.sleep(0.5)


def wait_window_close_finish():
    time.sleep(1)


def type_with_delay(*args):
    for arg in args:
        pyautogui.keyDown(str(arg))
        time.sleep(0.2)
    for arg in args:
        pyautogui.keyUp(str(arg))
        time.sleep(0.2)
    pyautogui.hotkey('esc')


def close_current_window():
    type_with_delay('alt', 'space', 'c')
    wait_window_close_finish()


def maximize_current_window():
    type_with_delay('alt', 'space', 'x')
    wait_window_maximize_finish()
