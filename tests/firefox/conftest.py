import pytest

from core.enums.app_name import AppName
from core.helpers.app_details import AppDetails
from core.helpers.app_manager import AppManager
from core.helpers.test_collector import TestReport, collect_test_results
from core.image_search.image_search import update_image_assets


def pytest_runtest_logreport(report: TestReport):
    return collect_test_results(report)


@pytest.fixture(scope="session", autouse=True)
def load_app_manager(request):
    # called once at beginning

    app_details = AppDetails(AppName.FIREFOX, with_custom_path=False)
    app_manager: AppManager = AppManager(app_details, with_web_driver=True)

    update_image_assets(app_manager.get_image_assets())
    pytest.app_manager = app_manager

    def clear_app_manager():
        pytest.app_manager.close_app()

    request.addfinalizer(clear_app_manager)
