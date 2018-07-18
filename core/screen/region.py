from typing import List

from core.default_settings import DefaultSettings
from core.enums.tesseract_language_code import LanguageCode
from core.helpers.point import Point
from core.highlight.screen_highlight import ScreenHighlight
from core.image_search.image_search import image_find, image_find_all, image_wait
from core.screen.screen_rectangle import ScreenRectangle
from core.text_search.ocr_result import OcrResult
from core.text_search.text_search import region_to_string, region_to_data


class Region:
    def __init__(self, start_point: Point, width: int, height: int):
        self._region_area: ScreenRectangle = ScreenRectangle(start_point, width, height)

    def highlight(self, seconds: float = None):
        highlight = ScreenHighlight()

        highlight.draw_rectangle(self._region_area.to_highlight_rectangle())

        if seconds is None:
            seconds = DefaultSettings.HIGHLIGHT_DURATION.value

        highlight.render(int(seconds * 1000))
        # time.sleep(seconds)

    def image_find(self, image_name: str, precision: int = None) -> Point or Exception:
        self.highlight()
        return image_find(image_name, self._region_area, precision)

    def image_find_all(self, image_name: str, precision: int = None) -> List[Point] or Exception:
        self.highlight()
        return image_find_all(image_name, self._region_area, precision)

    def image_wait(self, image_name: str, precision: int = None, wait_seconds: float = None) -> Point or Exception:
        self.highlight()
        return image_wait(image_name, self._region_area, precision, wait_seconds)

    def get_text(self, lang: LanguageCode = None) -> str:
        return region_to_string(self._region_area, lang)

    def get_ocr_results(self, lang: LanguageCode = None) -> List[OcrResult]:
        return region_to_data(self._region_area, lang)
