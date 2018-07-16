import time
from typing import List

import cv2
import numpy as np
import pyautogui

from core.default_settings import DefaultSettings
from core.enums.color import Color
from core.helpers.os_helpers import is_retina
from core.helpers.point import Point
from core.screen.screen_rectangle import ScreenRectangle
from core.highlight.highlight_rectangle import HighlightRectangle
from core.highlight.screen_highlight import ScreenHighlight
from core.image_search.asset_image import AssetImage
from core.screen.screenshot_image import ScreenshotImage

pyautogui.FAILSAFE = False
_cv_match_method = cv2.TM_CCOEFF_NORMED
_images = {}


def update_image_assets(new_images: dict):
    global _images
    _images = new_images


def _match_template(asset_name: str, screen_coordinates: ScreenRectangle = None,
                    precision: int = None) -> Point or None:
    if precision is None:
        precision = DefaultSettings.SEARCH_MIN_PRECISION.value

    screen_img = ScreenshotImage(screen_coordinates)
    asset_img = AssetImage(asset_name, _images[asset_name])

    res = cv2.matchTemplate(screen_img.image_gray_array, asset_img.image_gray_array, _cv_match_method)
    min_val, max_val, min_location, match = cv2.minMaxLoc(res)

    if max_val < precision:
        return None
    else:
        if is_retina():
            found_at = Point(match[0] / 2, match[1] / 2)
        else:
            found_at = Point(match[0], match[1])

        highlight = ScreenHighlight()
        highlight.draw_rectangle(HighlightRectangle(found_at, asset_img.width, asset_img.height, Color.GREEN, 2))

        highlight.render(int(DefaultSettings.HIGHLIGHT_DURATION.value * 1000))
        time.sleep(DefaultSettings.HIGHLIGHT_DURATION.value)

        return found_at


def _match_template_multiple(asset_name: str, screen_coordinates: ScreenRectangle, precision: int = None,
                             threshold: int = None) -> List[Point]:
    if precision is None:
        precision = DefaultSettings.SEARCH_MIN_PRECISION.value
    if threshold is None:
        threshold = DefaultSettings.SEARCH_THRESHOLD.value

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


def image_find(image_name: str, screen_coordinates: ScreenRectangle = None,
               precision: int = None) -> Point or Exception:
    if not isinstance(image_name, str):
        raise Exception('Invalid input type %s' % type(image_name))

    found = _match_template(image_name, screen_coordinates, precision)
    if found is not None and isinstance(found, Point):
        return found
    else:
        raise Exception('Unable to find %s' % image_name)


def image_find_all(image_name: str, screen_coordinates: ScreenRectangle = None, precision: int = None,
                   threshold: int = None) -> List[Point] or Exception:
    if not isinstance(image_name, str):
        raise Exception('Invalid input type %s' % type(image_name))

    list_of_finds: List[Point] = _match_template_multiple(image_name, screen_coordinates, precision, threshold)
    if len(list_of_finds) > 0:
        return list_of_finds
    else:
        raise Exception('Unable to find %s' % image_name)


def image_wait(image_name: str, screen_coordinates: ScreenRectangle = None, precision: int = None,
               wait_seconds: float = None) -> Point or Exception:
    if not isinstance(image_name, str):
        raise Exception('Invalid input type %s' % type(image_name))

    if wait_seconds is None:
        wait_seconds = DefaultSettings.WAIT_TIMEOUT.value

    start_time = time.time()
    current_duration = 0
    found = False

    while found is False and current_duration <= wait_seconds:
        print('Waiting %s for %s seconds' % (image_name, current_duration))
        found_coord = _match_template(image_name, screen_coordinates, precision)
        current_duration = round(float(time.time() - start_time), 2)
        if found_coord is not None and isinstance(found_coord, Point):
            return found_coord

    raise Exception('Waiting for %s image, unable to find it after %s seconds' % (image_name, wait_seconds))
