import cv2
import numpy as np
from pyautogui import screenshot
from pyautogui import size as get_screen_size

from core.screen.screen_rectangle import ScreenRectangle


class ScreenshotImage:
    def __init__(self, in_region: ScreenRectangle = None):
        screen_width, screen_height = get_screen_size()
        region_coordinates = (0, 0, screen_width, screen_height)

        if in_region is not None:
            region_coordinates = (in_region.start_point.x, in_region.start_point.y, in_region.width, in_region.height)

        screen_pil_image = screenshot(region=region_coordinates)

        self._gray_array = cv2.cvtColor(np.array(screen_pil_image), cv2.COLOR_BGR2GRAY)
        height, width = self._gray_array.shape
        self._width = width
        self._height = height

    @property
    def image_gray_array(self):
        return self._gray_array

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def binarize(self):
        # img2 = cv2.adaptiveThreshold(self._gray_array, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return cv2.threshold(self._gray_array, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
