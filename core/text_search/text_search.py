import pytesseract

from core.enums.default_paths import DefaultPaths
from core.helpers.os_helpers import get_os_platform
from core.image_search.screenshot_image import ScreenshotImage
from core.helpers.screen_rectangle import ScreenRectangle

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
