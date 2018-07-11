from enum import Enum


class DefaultPaths(Enum):
    WINDOWS = {
        'APPLICATIONS': ['C:\\Program Files (x86)', 'C:\\Program Files']
    }
    LINUX = {
        'APPLICATIONS': ['/bin', '/usr/bin', '/usr/share']
    }
    DARWIN = {
        'APPLICATIONS': ['~/Applications']
    }
