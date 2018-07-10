from enum import Enum

from core.enums.app_name import AppName


class CustomPaths(Enum):
    WINDOWS = {
        AppName.FIREFOX.name: 'C:\\Program Files\\Mozilla Firefox',
        AppName.INTERNET_EXPLORER.name: 'C:\\Program Files\\internet explorer'
    }
    LINUX = {
        AppName.FIREFOX.name: None,
        AppName.INTERNET_EXPLORER.name: None
    }
    DARWIN = {
        AppName.FIREFOX.name: '',
        AppName.INTERNET_EXPLORER.name: None
    }
