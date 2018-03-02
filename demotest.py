import pyautogui as gui
from imagesearch import *
import webbrowser as browser

browser.register('firefox', None, browser.GenericBrowser('firefox'), 1)
browser.get('firefox').open('https://stackoverflow.com')

gui.FAILSAFE = False

screenWidth, screenHeight = gui.size()
print("Available width:", screenWidth)
print("Available height:", screenHeight)

# Just a long move until figuring out how to wait for leBrowser to open
gui.moveTo(0, 0, 2)

imgAsStep = ["assets/reload.png", "assets/home.png", "assets/back.png"]

# Image find and click example
for toSearch in imgAsStep:
    pos = imagesearcharea(toSearch, 0, 0, screenWidth, 200)
    if pos[0] != -1:
        print("Found " + toSearch + " position : ", pos[0], pos[1])
        gui.moveTo(pos[0], pos[1])
        click_image(toSearch, pos, "left", 0.2, offset=5)
    else:
        print("Image not found:", toSearch)

# Mouse and keyboard example
gui.moveTo(600, 75)
gui.click(600, 75)
gui.hotkey('ctrl', 'a')
gui.typewrite(["delete"])
gui.typewrite('http://google.com', interval=0.1)
gui.typewrite(["enter"])
