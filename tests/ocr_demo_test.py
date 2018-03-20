from helpers.image_search import *
import pyautogui as gui
from time import sleep

screenWidth, screenHeight = gui.size()
menu = "assets/common/open_menu.png"
home = "assets/common/home.png"


def test_ocr():
    pos = imagesearch(menu)
    if pos[0] != -1:
        print("Found  position : ", pos[0], pos[1])
        click_image(menu, pos, "left", 0, offset=5)
        sleep(0.5)
        text_search("test", True)

    home_pos = imagesearch(home)
    click_image(home, home_pos, "left", 0, offset=5)
