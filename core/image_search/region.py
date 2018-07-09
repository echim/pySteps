from core.helpers.point import Point
from core.helpers.screen_area import ScreenArea
from core.image_search.image_search import find, find_all


class Region:
    def __init__(self, region_area: ScreenArea):
        self._region_area = region_area

    def find(self, image_name: str, precision: int = None) -> Point or Exception:
        return find(image_name, self._region_area, precision)

    def find_all(self, image_name: str, precision: int = None):
        return find_all(image_name, self._region_area, precision)
