from helpers.image_search import *
from time import sleep

menu = "open_menu.png"
home = "home.png"


def test_ocr():
    pos = find(menu)
    if pos[0] != -1:
        print("Found  position : ", pos[0], pos[1])
        click(menu)
        sleep(0.5)

    click(home)
