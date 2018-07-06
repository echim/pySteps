import numpy as np
import cv2
from pyautogui import screenshot
from pyautogui import size as get_screen_size
from helpers.general.rectangle import Rectangle


class ScreenImage:
    def __init__(self, in_region: Rectangle = None):
        screen_width, screen_height = get_screen_size()
        region_coordinates = (0, 0, screen_width, screen_height)

        if in_region is not None:
            region_coordinates = (in_region.start_point.x, in_region.start_point.y, in_region.width, in_region.height)

        screen_pil_image = screenshot(region=region_coordinates)

        self._image_gray_array = cv2.cvtColor(np.array(screen_pil_image), cv2.COLOR_BGR2GRAY)
        width, height = self._image_gray_array.shape
        self._width = width
        self._height = height

    @property
    def image_gray_array(self):
        return self._image_gray_array

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
