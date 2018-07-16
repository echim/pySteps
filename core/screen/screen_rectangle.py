from core.default_settings import DefaultSettings
from core.enums.color import Color
from core.helpers.point import Point
from core.helpers.rectangle import Rectangle
from core.highlight.highlight_rectangle import HighlightRectangle


class ScreenRectangle(Rectangle):
    def __init__(self, start_point: Point, width: int, height: int):
        Rectangle.__init__(self, start_point, width, height)

    def to_highlight_rectangle(self, color: Color = Color.RED, thickness: int = None) -> HighlightRectangle:
        if thickness is None:
            thickness = DefaultSettings.HIGHLIGHT_THICKNESS.value
        return HighlightRectangle(self._start_point, self._width, self._height, color, thickness)
