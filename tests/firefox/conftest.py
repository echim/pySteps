import pytest

from core.enums.app_name import AppName
from core.enums.pytest_outcome import TestOutcome
from core.helpers.app_details import AppDetails
from core.helpers.app_manager import AppManager
from core.image_search.image_search import update_image_assets


def pytest_runtest_logreport(report):
    if report.when == 'call':
        test_results = {
            'test': report.nodeid,
            'status': report.outcome,
            'duration': report.duration
        }
        if report.outcome == TestOutcome.FAILED.value:
            test_results['error'] = report.longrepr


@pytest.fixture(scope="session", autouse=True)
def load_app_manager(request):
    # called once at beginning

    app_details = AppDetails(AppName.FIREFOX, True)
    app_manager: AppManager = AppManager(app_details, with_web_driver=True)

    update_image_assets(app_manager.get_image_assets())
    pytest.app_manager = app_manager

    def clear_app_manager():
        pytest.app_manager.close_app()

    request.addfinalizer(clear_app_manager)
