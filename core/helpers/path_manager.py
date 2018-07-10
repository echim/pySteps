import os
from enum import Enum

from core.default_settings import DefaultSettings
from core.helpers.app_name import AppName
from core.helpers.os_helpers import OsPlatform, get_os_platform, get_project_root_path, Extension, \
    load_files, is_platform_windows, get_app_full_name, get_app_base_name


class DefaultPaths(Enum):
    WINDOWS = {
                  'APPLICATIONS': ['C:\\Program Files (x86)', 'C:\\Program Files']
              },
    LINUX = {
                'APPLICATIONS': ['/bin', '/usr/bin', '/usr/share']
            },
    DARWIN = {
        'APPLICATIONS': ['~/Applications']
    }


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


class PathManager:

    def get_platform_applications_paths(self) -> list:
        if self.custom_executable_path is not None:
            if os.path.exists(self.custom_executable_path):
                return [self.custom_executable_path]
            else:
                raise Exception('Path not found: %s' % self.custom_executable_path)
        else:
            if self.platform == OsPlatform.WINDOWS:
                app_paths = DefaultPaths[OsPlatform.WINDOWS.name]['APPLICATIONS']
            elif self.platform == OsPlatform.LINUX:
                app_paths = DefaultPaths[OsPlatform.LINUX.name]['APPLICATIONS']
            elif self.platform == OsPlatform.OSX:
                app_paths = DefaultPaths[OsPlatform.DARWIN.name]['APPLICATIONS']
            else:
                raise Exception('Unknown app paths for %s platform' % self.platform.value)

            return app_paths

    @staticmethod
    def get_image_assets_path(app_name: str = None) -> list:
        project_root_path = get_project_root_path()
        app_name = get_app_base_name(app_name) if app_name is not None else ''

        image_assets_path = os.path.join(project_root_path, 'tests', app_name, 'assets')

        if not os.path.exists(image_assets_path):
            raise Exception('Image assets path does not exist: %s' % image_assets_path)
        return [image_assets_path]

    def find_app_path_by_name(self, app_name: str) -> str:
        of_extension: Extension = Extension.EXE if is_platform_windows() else None
        app_full_name = get_app_full_name(app_name)
        all_executables = load_files(self.get_platform_applications_paths(), of_extension)

        if app_full_name in all_executables.keys():
            return all_executables[app_full_name]
        else:
            raise Exception('Unable to find executable %s in %s' % (app_name, self.get_platform_applications_paths()))

    def get_img_assets(self, app_name: str = None) -> dict:
        image_assets_path = self.get_image_assets_path(app_name)
        within_parent_folders = ['common', get_os_platform().value]

        all_images = load_files(image_assets_path, Extension.PNG, in_folders=within_parent_folders)

        if DefaultSettings.CONFIRM_LAUNCH_NAME.value in all_images.keys():
            return all_images
        else:
            raise Exception(
                'Unable to locate %s file inside %s' % (DefaultSettings.CONFIRM_LAUNCH_NAME.value, image_assets_path))

    def get_html_assets(self, app_name: str = None) -> dict:
        within_parent_folders = ['common', get_os_platform().value]
        return load_files(self.get_image_assets_path(app_name), Extension.HTML, in_folders=within_parent_folders)

    def __init__(self, custom_executable_path: str = None):
        self.platform = get_os_platform()
        self.custom_executable_path: str = custom_executable_path
