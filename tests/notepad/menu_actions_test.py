from core.test_dependencies import *


@pytest.mark.skipif(platform_is_other_than_windows(), reason='notepad should only be tested on Windows')
def test_get_text():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    typewrite("Hello world ")

    left_corner = Region(Point(0, 0), 350, 200)
    left_corner.highlight(3)

    left_corner_text = left_corner.get_text()
    assert 'Hello world' in left_corner_text

    app_manager.close_app()


@pytest.mark.skipif(platform_is_other_than_windows(), reason='notepad should only be tested on Windows')
def test_open_about_notepad():
    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    press('alt')
    press(['right', 'right', 'right', 'right'])
    press(['enter', 'down', 'enter'])

    left_corner = Region(Point(0, 0), 500, 500)
    left_corner.highlight(2)

    left_corner.image_find('logo_big.png')

    app_manager.close_app()
