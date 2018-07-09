from core.helpers.color import Color
from core.helpers.rectangle import *


class HighlightRectangle(Rectangle):
    def __init__(self, start_point: Point, width: int, height: int, color: Color = Color.GREEN, thickness: int = 2):
        Rectangle.__init__(self, start_point, width, height)
        self._color: Color = color
        self._thickness: int = thickness

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: Color):
        self._color = new_color.value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, new_thickness: int):
        self._thickness = new_thickness
