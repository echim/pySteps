import pytest
from pyautogui import typewrite, hotkey

from core.enums.tesseract_language_code import LanguageCode
from core.helpers.app_manager import AppManager
from core.screen.screen import Screen


def check_ocr_for_word(word: str):
    typewrite('%s ' % word)
    screen_text = Screen.get_text(LanguageCode.ENGLISH)
    assert word in screen_text
    hotkey('ctrl', 'a')
    hotkey('delete')


def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    words = ['word', 'test', 'notepad', 'application', 'file', 'edit', 'view']
    for word_to_check in words:
        check_ocr_for_word(word_to_check)

    app_manager.close_app()
