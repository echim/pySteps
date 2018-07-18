from typing import List

import pytesseract

from core.default_settings import DefaultSettings
from core.enums.default_paths import DefaultPaths
from core.enums.tesseract_language_code import LanguageCode
from core.helpers.os_helpers import get_os_platform
from core.helpers.point import Point
from core.screen.screen_rectangle import ScreenRectangle
from core.screen.screenshot_image import ScreenshotImage
from core.text_search.ocr_result import OcrResult

pytesseract.pytesseract.tesseract_cmd = DefaultPaths[get_os_platform().name].value['TESSERACT']


def image_to_string(image: ScreenshotImage = None, lang: LanguageCode = None) -> str:
    '''

    :param image: Image to extract text from.
    :param lang: Tesseract language code.
    :return: All text from image as string.
    '''
    if lang is None:
        lang = DefaultSettings.OCR_LANGUAGE
    if image is None:
        image = ScreenshotImage()
    return pytesseract.image_to_string(image.binarize(), lang.value)


def region_to_string(screen_coordinates: ScreenRectangle, lang: LanguageCode = None) -> str:
    '''

    :param screen_coordinates: Smaller region of the entire screen to extract text from.
    :param lang: Tesseract language code.
    :return: All text from region as string.
    '''
    screen_img = ScreenshotImage(screen_coordinates)
    return image_to_string(screen_img, lang)


def image_to_data(image: ScreenshotImage = None, lang: LanguageCode = None) -> List[OcrResult]:
    '''

    :param image: Image to extract data including boxes and confidences.
    :param lang: Tesseract language code.
    :return: All ocr results.
    '''
    if lang is None:
        lang = DefaultSettings.OCR_LANGUAGE
    if image is None:
        image = ScreenshotImage()

    tess_data = pytesseract.image_to_data(image.binarize(), output_type=pytesseract.Output.DICT, lang=lang.value)
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


def region_to_data(screen_coordinates: ScreenRectangle, lang: LanguageCode = None) -> List[OcrResult]:
    '''

    :param screen_coordinates: Smaller region of screen to extract data including boxes and confidences.
    :param lang: Tesseract language code.
    :return: All the ocr results.
    '''
    screen_img = ScreenshotImage(screen_coordinates)
    return image_to_data(screen_img, lang)
