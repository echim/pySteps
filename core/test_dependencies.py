import pytest

from core.helpers.app_manager import AppManager
from core.helpers.point import Point
from core.screen.screen import Screen
from core.screen.region import Region
from core.helpers.os_helpers import platform_is_other_than_windows
from pyautogui import typewrite, press
from core.mouse_commands.mouse_commands import move_pointer_to_image, move_pointer
from core.keyboard_commands.keyboard_commands import maximize_current_window, close_current_window
