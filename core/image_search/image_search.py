import time

import cv2
import numpy as np
import pyautogui
from typing import List

from core.helpers.color import Color
from core.helpers.point import Point
from core.helpers.rectangle import Rectangle
from core.highlight.highlight_rectangle import HighlightRectangle
from core.highlight.screen_highlight import ScreenHighlight
from core.image_search.asset_image import AssetImage
from core.image_search.screenshot_image import ScreenshotImage

pyautogui.FAILSAFE = False
_img_match_precision = 0.8
_cv_match_method = cv2.TM_CCOEFF_NORMED
_images = {}


# pytesseract.pytesseract.tesseract_cmd

def update_image_assets(new_images: dict):
    global _images
    _images = new_images


def _match_template(asset_name: str, screen_coordinates: Rectangle = None, precision=_img_match_precision):
    screen_img = ScreenshotImage(screen_coordinates)
    asset_img = AssetImage(asset_name, _images[asset_name])

    res = cv2.matchTemplate(screen_img.image_gray_array, asset_img.image_gray_array, _cv_match_method)
    min_val, max_val, min_location, best_match = cv2.minMaxLoc(res)

    if max_val < precision:
        return None
    else:
        found_at = Point(best_match[0], best_match[1])

        highlight = ScreenHighlight()
        highlight.draw_rectangle(HighlightRectangle(found_at, asset_img.width, asset_img.height, Color.GREEN, 2))
        highlight.render(1000)
        time.sleep(1)

        return found_at


def _match_template_multiple(asset_name: str, screen_coordinates: Rectangle, precision=_img_match_precision,
                             threshold=0.9) -> List[Point]:
    screen_img = ScreenshotImage(screen_coordinates)
    asset_img = AssetImage(asset_name, _images[asset_name])

    res = cv2.matchTemplate(screen_img.image_gray_array, asset_img.image_gray_array, _cv_match_method)

    final_matches = []
    while True:
        min_val, max_val, min_loc, best_match = cv2.minMaxLoc(res)
        if _cv_match_method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = best_match

        if precision > max_val > threshold:
            sx, sy = top_left
            for x in range(sx - asset_img.width / 2, sx + asset_img.width / 2):
                for y in range(sy - asset_img.height / 2, sy + asset_img.height / 2):
                    try:
                        res[y][x] = np.float32(-10000)
                    except IndexError:
                        pass
            new_match_point = Point(top_left[0], top_left[1])
            final_matches.append(new_match_point)
        else:
            break

    return final_matches


def _image_search(asset_name: str, in_region: Rectangle = None, precision: int = _img_match_precision):
    return _match_template(asset_name, in_region, precision)


def _image_search_multiple(asset_name: str, in_region: Rectangle = None, precision: int = _img_match_precision):
    return _match_template_multiple(asset_name, in_region, precision)


def find(asset_name: str) -> Point or Exception:
    if not isinstance(asset_name, str):
        raise Exception('Invalid input type %s' % type(asset_name))

    found = _image_search(asset_name)
    if found is not None and isinstance(found, Point):
        return found
    else:
        raise Exception('Unable to find %s' % asset_name)


def find_all(image_name: str) -> List[Point]:
    return _image_search_multiple(image_name)
