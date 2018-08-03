from core.test_dependencies import *


# https://docs.pytest.org/en/2.9.0/skipping.html
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_raises(record_property):
    record_property("description", 'This is an example of test that will throw error.')
    return 9 / 0


# https://docs.pytest.org/en/2.9.0/usage.html?highlight=pdb
def test_with_debug(record_property):
    record_property("description", 'This is an example of test with debug.')
    # pytest.set_trace()
    pass


# Firefox without selenium example
def test_image_search(record_property):
    record_property("description", 'This is a demo test for Firefox.')

    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app('-foreground -new-instance -private')

    found_coord = Screen.image_find('reload.png')
    assert isinstance(found_coord, Point)

    Region(Point(0, 0), 500, 500).image_find('reload.png')

    app_manager.close_app()
