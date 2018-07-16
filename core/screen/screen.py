from typing import List

from core.helpers.point import Point
from core.image_search.image_search import image_find, image_find_all, image_wait
from core.text_search.ocr_result import OcrResult
from core.text_search.text_search import image_to_string, image_to_data


class Screen:
    @staticmethod
    def image_find(image_name: str, precision: int = None) -> Point or Exception:
        return image_find(image_name, None, precision)

    @staticmethod
    def image_find_all(image_name: str, precision: int = None) -> List[Point] or Exception:
        return image_find_all(image_name, None, precision)

    @staticmethod
    def image_wait(image_name: str, precision: int = None, wait_seconds: float = None) -> Point or Exception:
        return image_wait(image_name, None, precision, wait_seconds)

    @staticmethod
    def get_text() -> str:
        return image_to_string()

    @staticmethod
    def get_ocr_results() -> List[OcrResult]:
        return image_to_data()
