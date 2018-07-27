from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from core.enums.app_name import AppName


def get_options_from_string(extra_args: str, input_options):
    '''
    String of arguments to Options
    :param extra_args: String of arguments like: '-private -foreground'
    :param input_options: Empty Options object to populate.
    :return:
    '''
    args = extra_args.split()
    for arg in args:
        input_options.add_argument(str(arg))
    return input_options


def get_driver_by_app_name(app_name: str, extra_args: str):
    '''

    :param app_name: The app name string value. Ex: chrome, firefox
    :param extra_args: String of arguments like: '-private -foreground'
    :return:
    '''
    if app_name is AppName.EDGE.value:
        return webdriver.Edge()
    elif app_name is AppName.INTERNET_EXPLORER.value:
        return webdriver.Ie()
    elif app_name is AppName.FIREFOX.value:
        firefox_options = FirefoxOptions()
        return webdriver.Firefox(options=get_options_from_string(extra_args, firefox_options))
    elif app_name is AppName.CHROME.value:
        chrome_options = ChromeOptions()
        return webdriver.Chrome(options=get_options_from_string(extra_args, chrome_options))
    else:
        raise NotImplementedError('Loading %s app not implemented yet.' % app_name)
