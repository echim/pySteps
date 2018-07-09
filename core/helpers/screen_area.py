from core.helpers.point import Point
from core.helpers.rectangle import Rectangle


class ScreenArea(Rectangle):
    def __init__(self, start_point: Point, width: int, height: int):
        Rectangle.__init__(self, start_point, width, height)
