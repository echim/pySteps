from enum import Enum

from core.enums.tesseract_language_code import LanguageCode


class DefaultSettings(Enum):
    SEARCH_MIN_PRECISION = 0.8
    SEARCH_THRESHOLD = 0.99
    WAIT_TIMEOUT = 10.0
    HIGHLIGHT_DURATION = 0.4
    HIGHLIGHT_THICKNESS = 5
    OCR_MIN_CONFIDENCE = 50
    OCR_LANGUAGE = LanguageCode.ENGLISH.value
    CONFIRM_LAUNCH_NAME = 'confirm_app_launch.png'
    LOG_FILE_NAME = 'pyTest_runs.log'
