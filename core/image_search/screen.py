from core.helpers.point import Point
from core.image_search.image_search import find, find_all


class Screen:
    @staticmethod
    def find(image_name: str, precision: int = None) -> Point or Exception:
        return find(image_name, None, precision)

    @staticmethod
    def find_all(image_name: str, precision: int = None):
        return find_all(image_name, None, precision)
