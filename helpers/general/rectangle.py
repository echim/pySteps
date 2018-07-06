from helpers.general.point import Point


class Rectangle:
    def __init__(self, start_point: Point, width: int, height: int):
        self._start_point: Point = start_point
        self._width: int = width
        self._height: int = height

    @property
    def start_point(self) -> Point:
        return self._start_point

    @start_point.setter
    def start_point(self, new_point: Point):
        self._start_point = new_point

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, new_width: int):
        self._width = new_width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, new_height: int):
        self._height = new_height
