import pytest

from core.helpers.app_details import AppDetails
from core.helpers.app_manager import AppManager
from core.enums.app_name import AppName
from core.image_search.image_search import update_image_assets


@pytest.fixture(scope="session", autouse=True)
def load_app_manager(request):
    # called once at beginning

    app_details = AppDetails(AppName.INTERNET_EXPLORER, True)
    app_manager: AppManager = AppManager(app_details)

    update_image_assets(app_manager.get_image_assets())
    pytest.app_manager = app_manager

    def clear_app_manager():
        pytest.app_manager = None

    request.addfinalizer(clear_app_manager)
