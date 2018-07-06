from os import path
import numpy as np
import cv2


class AssetImage:
    def __init__(self, image_name: str, image_path: str):
        self._image_name = image_name

        if path.exists(image_path):
            self._image_path = image_path
        else:
            raise Exception('Invalid AssetImage path: %s' % image_path)

        self._image_gray_array = cv2.imread(image_path, 0)
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
