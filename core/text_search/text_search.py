from typing import List

import pytesseract

from core.default_settings import DefaultSettings
from core.enums.default_paths import DefaultPaths
from core.helpers.os_helpers import get_os_platform
from core.helpers.point import Point
from core.image_search.screenshot_image import ScreenshotImage
from core.screen.screen_rectangle import ScreenRectangle
from core.text_search.ocr_result import OcrResult

pytesseract.pytesseract.tesseract_cmd = DefaultPaths[get_os_platform().name].value['TESSERACT']


def image_to_string(image: ScreenshotImage = None) -> str:
    '''

    :param image: Image to extract text from.
    :return: All text from image as string.
    '''
    if image is None:
        image = ScreenshotImage()
    return pytesseract.image_to_string(image.image_gray_array)


def region_to_string(screen_coordinates: ScreenRectangle) -> str:
    '''

    :param screen_coordinates: Smaller region of the entire screen to extract text from.
    :return: All text from region as string.
    '''
    screen_img = ScreenshotImage(screen_coordinates)
    return image_to_string(screen_img)


def image_to_data(image: ScreenshotImage = None) -> List[OcrResult]:
    '''

    :param image: Image to extract data including boxes and confidences.
    :return: All ocr results.
    '''
    if image is None:
        image = ScreenshotImage()

    tess_data = pytesseract.image_to_data(image.image_gray_array, output_type=pytesseract.Output.DICT)
    tess_data_len = len(tess_data['text'])
    all_ocr_results: List[OcrResult] = []

    for result_index in range(tess_data_len):
        if tess_data["conf"][result_index] > DefaultSettings.OCR_MIN_CONFIDENCE.value:
            ocr_find = OcrResult(
                Point(tess_data['left'][result_index], tess_data['top'][result_index]),
                tess_data['width'][result_index],
                tess_data['height'][result_index],
                tess_data['text'][result_index])
            all_ocr_results.append(ocr_find)

    return all_ocr_results


def region_to_data(screen_coordinates: ScreenRectangle) -> List[OcrResult]:
    '''

    :param screen_coordinates: Smaller region of screen to extract data including boxes and confidences.
    :return: All the ocr results.
    '''
    screen_img = ScreenshotImage(screen_coordinates)
    return image_to_data(screen_img)
