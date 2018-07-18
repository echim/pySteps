from typing import List

from core.enums.tesseract_language_code import LanguageCode
from core.helpers.point import Point
from core.image_search.image_search import image_find, image_find_all, image_wait
from core.mouse_commands.mouse_commands import move_pointer, move_pointer_to_image
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
    def image_wait(image_name: str, wait_seconds: float = None, precision: int = None) -> Point or Exception:
        return image_wait(image_name, wait_seconds, None, precision)

    @staticmethod
    def get_text(lang: LanguageCode = None) -> str:
        return image_to_string(lang=lang)

    @staticmethod
    def get_ocr_results(lang: LanguageCode = None) -> List[OcrResult]:
        return image_to_data(lang=lang)

    @staticmethod
    def move_pointer(destination: Point):
        move_pointer(destination)

    @staticmethod
    def move_pointer_to_image(image_name: str):
        move_pointer_to_image(image_name)
