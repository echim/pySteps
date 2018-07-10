from core.enums.color import Color
from core.helpers.circle import *


class HighlightCircle(Circle):
    def __init__(self, center: Point, radius: int, color: Color = Color.GREEN, thickness: int = 2):
        Circle.__init__(self, center, radius)
        self._color = color
        self._thickness = thickness

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
