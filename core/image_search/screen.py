from typing import List
from core.helpers.point import Point
from core.image_search.image_search import find, find_all, wait_find


class Screen:
    @staticmethod
    def find(image_name: str, precision: int = None) -> Point or Exception:
        return find(image_name, None, precision)

    @staticmethod
    def find_all(image_name: str, precision: int = None) -> List[Point] or Exception:
        return find_all(image_name, None, precision)

    @staticmethod
    def wait_find(image_name: str, precision: int = None, wait_seconds: float = None) -> Point or Exception:
        return wait_find(image_name, None, precision, wait_seconds)
