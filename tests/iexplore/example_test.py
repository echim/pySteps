from core.test_dependencies import *


@pytest.mark.skip(reason="This is just an example of mark.skip")
def test_will_fail():
    Screen.image_find('image_not_found.png')


@pytest.mark.skipif(platform_is_other_than_windows(), reason='iexplore should be only tested on Windows')
def test_image_search():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    Screen.image_find('forward.png')
    Region(Point(0, 0), 200, 200).image_find('forward.png')

    app_manager.close_app()
