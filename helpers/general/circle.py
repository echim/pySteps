from helpers.general.point import Point


class Circle:

    def __init__(self, center: Point, radius: int):
        self._center: Point = center
        self._radius: int = radius

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
