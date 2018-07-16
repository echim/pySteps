from enum import Enum


class DefaultSettings(Enum):
    SEARCH_MIN_PRECISION = 0.8
    SEARCH_THRESHOLD = 0.99
    WAIT_TIMEOUT = 10.0
    HIGHLIGHT_DURATION = 0.4
    HIGHLIGHT_THICKNESS = 5
    OCR_MIN_CONFIDENCE = 50
    CONFIRM_LAUNCH_NAME = 'confirm_app_launch.png'
