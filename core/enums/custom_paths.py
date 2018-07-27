from enum import Enum

from core.enums.app_name import AppName


class CustomPaths(Enum):
    WINDOWS = {
        AppName.NOTEPAD.name: 'C:\\Windows\\system32'
    }
    LINUX = {
        AppName.NOTEPAD.name: None
    }
    DARWIN = {
        AppName.NOTEPAD.name: None
    }
