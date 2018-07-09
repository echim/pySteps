import pytest

from core.image_search.image_search import *
from core.helpers.app_manager import AppManager


def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    time.sleep(5)
    find('forward.png')

    app_manager.close_app()
