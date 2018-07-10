import time
from typing import List

from core.default_settings import DefaultSettings
from core.helpers.point import Point
from core.helpers.screen_rectangle import ScreenRectangle
from core.highlight.screen_highlight import ScreenHighlight
from core.image_search.image_search import find, find_all, wait_find


class Region:
    def __init__(self, start_point: Point, width: int, height: int):
        self._region_area: ScreenRectangle = ScreenRectangle(start_point, width, height)

    def highlight(self, seconds: float = None):
        highlight = ScreenHighlight()

        highlight.draw_rectangle(self._region_area.to_highlight_rectangle())

        if seconds is None:
            seconds = DefaultSettings.HIGHLIGHT_DURATION.value

        highlight.render(int(seconds * 1000))
        time.sleep(seconds)

    def find(self, image_name: str, precision: int = None) -> Point or Exception:
        self.highlight()
        return find(image_name, self._region_area, precision)

    def find_all(self, image_name: str, precision: int = None) -> List[Point] or Exception:
        self.highlight()
        return find_all(image_name, self._region_area, precision)

    def find_wait(self, image_name: str, precision: int = None, wait_seconds: float = None) -> Point or Exception:
        self.highlight()
        return wait_find(image_name, self._region_area, precision, wait_seconds)
