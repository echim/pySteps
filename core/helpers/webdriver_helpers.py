from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from core.enums.app_name import AppName


def get_webdriver_by_app_name(app_name: str, extra_args: str):
    if app_name is AppName.EDGE.value:
        return webdriver.Edge()
    elif app_name is AppName.INTERNET_EXPLORER.value:
        return webdriver.Ie()
    elif app_name is AppName.FIREFOX.value:
        options: Options = Options()
        args = extra_args.split()
        for arg in args:
            options.add_argument(str(arg))
        return webdriver.Firefox(options=options)
