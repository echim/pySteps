import pytest

from core.helpers.app_manager import AppManager
from core.image_search.screen import Screen


def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    Screen.find('forward.png')

    app_manager.close_app()
