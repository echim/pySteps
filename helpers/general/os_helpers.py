import os
import platform
from enum import Enum
import time


class OsPlatforms(Enum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    OSX = 'Darwin'


class Extensions(Enum):
    EXE = '.exe'
    PNG = '.png'


class WinDefaultPaths(Enum):
    P_FILES_86 = 'C:\\Program Files (x86)'
    P_FILES_64 = 'C:\\Program Files'


def load_files(root_folders: list, extension: str = None, with_name: str = None) -> dict:
    '''

    :param extension : Extension of files
    :param root_folders: The parent folder
    :param with_name: The exact name of file
    :return: List of results
    '''
    all_files = {}

    start = time.time()
    for root_folder in root_folders:
        for root, dirs, files in os.walk(root_folder):
            for file_name in files:
                app_found = False
                if extension is not None and extension != '':
                    if file_name.endswith('%s' % extension):
                        app_found = True
                if with_name is not None:
                    if with_name == file_name:
                        app_found = True
                if app_found:
                    all_files[file_name] = os.path.join(root, file_name)

    print('Loaded all %s files from %s in %f seconds' % (extension, root_folders, (time.time() - start)))
    return all_files


def get_os() -> OsPlatforms:
    current_system = platform.system().upper()
    if OsPlatforms[current_system]:
        return OsPlatforms[current_system]
    else:
        raise Exception('Unknown os platform')
