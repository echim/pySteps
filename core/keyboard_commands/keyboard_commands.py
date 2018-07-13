import time

import pyautogui
from core.helpers.os_helpers import platform_is_darwin, platform_is_linux, platform_is_windows


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
    if platform_is_windows():
        type_with_delay('alt', 'space', 'c')
    if platform_is_linux():
        type_with_delay('alt', 'f4')
    wait_window_close_finish()


def maximize_current_window():
    if platform_is_windows():
        type_with_delay('alt', 'space', 'x')
    if platform_is_linux():
        type_with_delay('apps', 'up')

    wait_window_maximize_finish()
