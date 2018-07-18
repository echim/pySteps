from selenium import webdriver

from core.enums.app_name import AppName


def get_webdriver_by_app_name(app_name: str):
    if app_name is AppName.EDGE.value:
        return webdriver.Edge()
    elif app_name is AppName.INTERNET_EXPLORER.value:
        return webdriver.Ie()
    elif app_name is AppName.FIREFOX.value:
        return webdriver.Firefox()
