import os
import platform
import time

from core.enums.extension import Extension
from core.enums.os_platform import OsPlatform


def get_project_root_path():
    current_path = os.path.split(__file__)[0]
    return os.path.realpath(current_path.split('core')[0])


def load_files(root_folders: list, extension: Extension = None, with_name: str = None, in_folders: list = None) -> dict:
    '''

    :param extension : Extension of files
    :param root_folders: The root folder from where search begins
    :param with_name: The exact name of file
    :param in_folders: If file must be in certain folder name
    :return: List of results
    '''
    all_files = {}

    start = time.time()
    for root_folder in root_folders:
        for root, dirs, files in os.walk(root_folder):
            for file_name in files:
                if extension is not None:
                    if file_name.endswith('%s' % extension.value):
                        all_files[file_name] = os.path.join(root, file_name)
                if with_name is not None:
                    if with_name == file_name:
                        all_files[file_name] = os.path.join(root, file_name)
                if in_folders is not None:
                    for folder in in_folders:
                        if folder in root:
                            all_files[file_name] = os.path.join(root, file_name)

    total_time = time.time() - start
    print('Loaded %s (%s) files from %s in %f seconds' % (len(all_files), extension, root_folders, total_time))
    return all_files


def get_os_platform() -> OsPlatform:
    current_system = platform.system().upper()
    if OsPlatform[current_system]:
        return OsPlatform[current_system]
    else:
        raise Exception('Unknown os platform')


def is_platform_windows() -> bool:
    return get_os_platform() == OsPlatform.WINDOWS


def get_app_base_name(app_name: str = None) -> str or None:
    if app_name is None:
        return None
    elif '.' in app_name:
        return app_name[:app_name.index('.')]
    else:
        return app_name


def get_app_full_name(app_name: str = None) -> str or None:
    if app_name is None:
        return None

    base_name: str = get_app_base_name(app_name)
    return base_name + Extension.EXE.value if is_platform_windows() else base_name
