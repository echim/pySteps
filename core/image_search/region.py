import time

from core.helpers.point import Point
from core.helpers.screen_rectangle import ScreenRectangle
from core.highlight.highlight_rectangle import HighlightRectangle
from core.highlight.screen_highlight import ScreenHighlight
from core.image_search.image_search import find, find_all


class Region:
    def __init__(self, start_point: Point, width: int, height: int):
        self._region_area: ScreenRectangle = ScreenRectangle(start_point, width, height)

    def highlight(self, seconds: int = 1):
        start_point = self._region_area.start_point
        width = self._region_area.width
        height = self._region_area.height

        highlight = ScreenHighlight()
        highlight.draw_rectangle(HighlightRectangle(start_point, width, height))

        highlight.render(int(seconds * 1000))
        time.sleep(seconds)

    def find(self, image_name: str, precision: int = None) -> Point or Exception:
        self.highlight()
        return find(image_name, self._region_area, precision)

    def find_all(self, image_name: str, precision: int = None):
        self.highlight()
        return find_all(image_name, self._region_area, precision)
