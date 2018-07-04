from helpers.general.color import Color
from helpers.general.point import Point


class HighlightCircle:

    def __init__(self, center: Point, radius: int, color: Color, width: int):
        self._center = center
        self._radius = radius
        self._color = color.value
        self._width = width

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, new_center: Point):
        self._center = new_center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius: int):
        self._radius = new_radius

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: Color):
        self._color = new_color.value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width: int):
        self._width = new_width
