import os
import platform
from enum import Enum
import time


class OsPlatforms(Enum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    OSX = 'Darwin'


class Extension(Enum):
    EXE = '.exe'
    PNG = '.png'
    HTML = '.html'


class WinDefaultPaths(Enum):
    PROGRAM_FILES_86 = 'C:\\Program Files (x86)'
    PROGRAM_FILES_64 = 'C:\\Program Files'


def get_project_root_path():
    current_path = os.path.split(__file__)[0]
    return os.path.realpath(current_path.split('helpers')[0])


def load_files(root_folders: list, extension: Extension = None, with_name: str = None, parent_name: str = None) -> dict:
    '''

    :param extension : Extension of files
    :param root_folders: The root folder from where search begins
    :param with_name: The exact name of file
    :param parent_name: If file must be in certain folder name
    :return: List of results
    '''
    all_files = {}

    start = time.time()
    for root_folder in root_folders:
        for root, dirs, files in os.walk(root_folder):
            for file_name in files:
                file_found = False
                if extension is not None:
                    file_found = True if file_name.endswith('%s' % extension.value) else False
                if with_name is not None:
                    file_found = True if with_name == file_name else False
                if parent_name is not None:
                    file_found = True if parent_name in root else False
                if file_found:
                    all_files[file_name] = os.path.join(root, file_name)

    print('Loaded all %s files from %s in %f seconds' % (extension, root_folders, (time.time() - start)))
    return all_files


def get_os_platform() -> OsPlatforms:
    current_system = platform.system().upper()
    if OsPlatforms[current_system]:
        return OsPlatforms[current_system]
    else:
        raise Exception('Unknown os platform')
