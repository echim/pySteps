import os

from core.helpers.os_helpers import WinDefaultPaths, OsPlatforms, get_os_platform, get_project_root_path, Extension, \
    load_files, is_platform_windows, get_app_full_name, get_app_base_name


class PathManager:

    def get_platform_applications_paths(self) -> list:
        if self.custom_executable_path is not None:
            if os.path.exists(self.custom_executable_path):
                return [self.custom_executable_path]
            else:
                raise Exception('Path not found: %s' % self.custom_executable_path)
        else:
            app_paths = []
            if self.platform == OsPlatforms.WINDOWS:
                app_paths.append(WinDefaultPaths.PROGRAM_FILES_86.value)
                app_paths.append(WinDefaultPaths.PROGRAM_FILES_64.value)
            elif self.platform == OsPlatforms.LINUX:
                raise Exception('Not Implemented')
            elif self.platform == OsPlatforms.OSX:
                raise Exception('Not Implemented')
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

    def get_app_path(self, app_name: str) -> str:
        of_extension: Extension = Extension.EXE if is_platform_windows() else None
        app_full_name = get_app_full_name(app_name)
        all_executables = load_files(self.get_platform_applications_paths(), of_extension)

        if app_full_name in all_executables.keys():
            return all_executables[app_full_name]
        else:
            raise Exception('Unable to find executable %s in %s' % (app_name, self.get_platform_applications_paths()))

    def get_img_assets(self, app_name: str = None) -> dict:
        within_parent_folders = ['common', get_os_platform().value]
        return load_files(self.get_image_assets_path(app_name), Extension.PNG, in_folders=within_parent_folders)

    def get_html_assets(self, app_name: str = None) -> dict:
        within_parent_folders = ['common', get_os_platform().value]
        return load_files(self.get_image_assets_path(app_name), Extension.HTML, in_folders=within_parent_folders)

    def __init__(self, custom_executable_path: str = None):
        self.platform = get_os_platform()
        self.custom_executable_path: str = custom_executable_path
