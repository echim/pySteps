from enum import Enum


class DefaultPaths(Enum):
    WINDOWS = {
        'APPLICATIONS': ['C:\\Program Files (x86)', 'C:\\Program Files'],
        'TESSERACT': 'C:\\tesseract\\build\\bin\\Release\\tesseract.exe'
    }
    LINUX = {
        'APPLICATIONS': ['/bin', '/usr/bin', '/usr/share'],
        'TESSERACT': ''
    }
    DARWIN = {
        'APPLICATIONS': ['/Applications'],
        'TESSERACT': ''
    }
