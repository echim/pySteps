from core.helpers.point import Point
from core.helpers.rectangle import Rectangle


class OcrResult(Rectangle):
    def __init__(self, start_point: Point, width: int, height: int, text: str):
        Rectangle.__init__(self, start_point, width, height)
        self._text = text

    @property
    def text(self):
        return self._text
