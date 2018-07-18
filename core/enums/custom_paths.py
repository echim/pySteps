from enum import Enum

from core.enums.app_name import AppName


class CustomPaths(Enum):
    WINDOWS = {
        AppName.FIREFOX.name: 'C:\\Program Files\\Mozilla Firefox',
        AppName.INTERNET_EXPLORER.name: 'C:\\Program Files\\internet explorer',
        AppName.NOTEPAD.name: 'C:\\Windows\\system32'
    }
    LINUX = {
        AppName.FIREFOX.name: '/usr/bin/',
        AppName.INTERNET_EXPLORER.name: None,
        AppName.NOTEPAD.name: None
    }
    DARWIN = {
        AppName.FIREFOX.name: '/Applications/Firefox.app',
        AppName.INTERNET_EXPLORER.name: None,
        AppName.NOTEPAD.name: None
    }
