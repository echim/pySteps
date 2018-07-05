import pytest
from helpers.general.app_manager import AppManager


def pytest_runtest_setup(item):
    # called before running each test in this directory
    print("> Setting up for: %s" % item.name)


@pytest.fixture(scope="session", autouse=True)
def load_app_manager(request):
    # called once at beginning
    app_mgr: AppManager = AppManager('firefox')
    app_mgr.launch_app()
    pytest.app_manager = app_mgr

    def clear_app_manager():
        pytest.app_manager = None

    request.addfinalizer(clear_app_manager)
