from pyautogui import moveTo

from core.helpers.point import Point
from core.image_search.image_search import image_wait, image_find
from core.screen.screen_rectangle import ScreenRectangle


def move_pointer(destination: Point):
    '''

    :param destination: The point where to move mouse pointer.
    :return: None
    '''
    moveTo(destination.x, destination.y)


def move_pointer_to_image(image_name: str, screen_coordinates: ScreenRectangle = None):
    '''

    :param image_name: Asset image name to look for and move the mouse pointer over.
    :param screen_coordinates: Region of screen where image should be.
    :return: None
    '''
    image_wait(image_name, 5.0, screen_coordinates)
    image_location: Point = image_find(image_name, screen_coordinates)
    move_pointer(image_location)
