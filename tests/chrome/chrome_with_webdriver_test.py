from core.test_dependencies import *


def test_chrome_demo(record_property):
    record_property("description", 'This is a demo test for Chrome featuring the ocr get_text.')

    app_manager: AppManager = pytest.app_manager
    app_manager.launch_app('--no-experiments --window-position=0,0')

    app_manager.browser.get('http://www.google.com/ncr')

    search_btn = app_manager.browser.find_element_by_name('btnK')
    search_size = search_btn.size
    search_loc = search_btn.location
    pad_top = 110

    btn_region = Region(Point(search_loc['x'], search_loc['y'] + pad_top), search_size['width'], search_size['height'])

    btn_region.highlight()
    assert 'Google Search' in btn_region.get_text(LanguageCode.ENGLISH)

    app_manager.browser.get('http://www.google.ro')
    btn_region.highlight()
    assert 'Căutare Google' in btn_region.get_text(LanguageCode.ROMANIAN)

    app_manager.close_app()
