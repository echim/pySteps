from os import path

import cv2

from core.helpers.os_helpers import is_retina


class AssetImage:
    def __init__(self, image_name: str, image_path: str):
        self._image_name = image_name

        if path.exists(image_path):
            self._image_path = image_path
        else:
            raise Exception('Invalid AssetImage path: %s' % image_path)

        self._image_gray_array = cv2.imread(image_path, 0)
        height, width = self._image_gray_array.shape
        self._width = width
        self._height = height

        if is_retina():
            self._width = 2 * width
            self._height = 2 * height
            self._image_gray_array = cv2.resize(self._image_gray_array,
                                                dsize=(self._width, self._height),
                                                interpolation=cv2.INTER_CUBIC)

    @property
    def image_gray_array(self):
        return self._image_gray_array

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
