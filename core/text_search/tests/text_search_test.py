import pytest
import time
from core.helpers.app_manager import AppManager
from core.helpers.point import Point
from core.screen.screen import Screen
from core.screen.region import Region


def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    Screen.get_text()

    screen_region = Region(Point(0, 0), 500, 500)
    screen_region.highlight()
    screen_region.get_text()

    app_manager.close_app()
