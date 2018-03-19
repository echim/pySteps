import pyautogui as gui
from helpers.image_search import *
import webbrowser as browser
import pytest


# Example of test that might throw errors that we want to ignore
# https://docs.pytest.org/en/2.9.0/skipping.html
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_raises():
    assert 1 == 1
    error = 9 / 0


# Example of test with debug
# https://docs.pytest.org/en/2.9.0/usage.html?highlight=pdb
def test_with_debug():
    string = 'test'
    # pytest.set_trace()


def test_dummy():
    browser.register('firefox', None, browser.GenericBrowser('firefox'), 1)
    browser.get('firefox').open('https://stackoverflow.com')
    gui.FAILSAFE = False

    screenWidth, screenHeight = gui.size()
    print("Available width:", screenWidth)
    print("Available height:", screenHeight)

    gui.moveTo(0, 0, 1)

    patterns = ["assets/common/reload.png", "assets/common/home.png", "assets/common/back.png"]

    browserStarted = imagesearch_loop(patterns[0], 2, attempts=3)
    assert browserStarted[0] != -1
    assert browserStarted[1] != -1

    # Image find and click example
    for toSearch in patterns:
        pos = imagesearcharea(toSearch, 0, 0, screenWidth, 200)
        if pos[0] != -1:
            print("Found " + toSearch + " position : ", pos[0], pos[1])
            gui.moveTo(pos[0], pos[1])
            click_image(toSearch, pos, "left", 0.2, offset=5)
        else:
            print("Image not found:", toSearch)

# Mouse and keyboard example
# gui.moveTo(600, 75)
# gui.click(600, 75)
# gui.hotkey('ctrl', 'a')
# gui.typewrite(["delete"])
# gui.typewrite('http://google.com', interval=0.1)
# gui.typewrite(["enter"])
