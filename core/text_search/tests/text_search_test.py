import pytest

from core.helpers.app_manager import AppManager
from core.screen.screen import Screen


def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    Screen.get_text()
    Screen.get_ocr_results()

    app_manager.close_app()
