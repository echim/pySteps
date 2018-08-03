from core.test_dependencies import *


@pytest.mark.skipif(platform_is_other_than_windows(), reason='notepad should only be tested on Windows')
def test_get_text(record_property):
    record_property("description", 'This is a demo test for Notepad with OCR example.')

    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    typewrite("Hello world ")

    left_corner = Region(Point(0, 0), 350, 200)
    left_corner.highlight(3)

    left_corner_text = left_corner.get_text()
    assert 'Hello world' in left_corner_text

    app_manager.close_app()


@pytest.mark.skipif(platform_is_other_than_windows(), reason='notepad should only be tested on Windows')
def test_open_about_notepad(record_property):
    record_property("description", 'This is a demo test for Notepad with image search example.')

    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app()

    press('alt')
    press(['right', 'right', 'right', 'right'])
    press(['enter', 'down', 'enter'])

    left_corner = Region(Point(0, 0), 500, 500)
    left_corner.highlight(2)

    left_corner.move_pointer_to_image('logo_big.png')
    move_pointer(Point(0, 0))
    close_current_window()

    app_manager.close_app()
