from core.test_dependencies import *


@pytest.mark.skipif(platform_is_other_than_windows(), reason='Edge should only be tested on Windows')
def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    app_manager.browser.get('http://www.google.com')
    assert app_manager.browser.title == 'Google'

    window_size = app_manager.browser.get_window_size()
    window_region = Region(Point(0, 0), window_size['width'], window_size['height'])
    window_region.highlight(5)
    window_region.image_find('home.png')

    app_manager.close_app()
