from helpers.general.os_helpers import WinDefaultPaths, OsPlatforms, get_os_platform, get_project_root_path, Extension, \
    load_files
import os


class PathManager:

    def get_application_paths(self) -> list:
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
        image_assets_path = os.path.join(project_root_path, 'assets', app_name if app_name is not None else '')

        if not os.path.exists(image_assets_path):
            raise Exception('Image assets path does not exist: %s' % image_assets_path)
        return [image_assets_path]

    def get_app_path(self, app_name: str) -> str:
        of_extension: Extension = Extension.EXE if self._on_windows else None
        app_full_name = app_name + Extension.EXE.value if self._on_windows else app_name
        all_executables = load_files(self.get_application_paths(), of_extension)

        if app_full_name in all_executables.keys():
            return all_executables[app_full_name]
        else:
            raise Exception('Unable to find executable %s in %s' % (app_name, self.get_application_paths()))

    def get_img_assets(self, app_name: str = None) -> dict:
        return load_files(self.get_image_assets_path(app_name), Extension.PNG)

    def get_html_assets(self, app_name: str = None) -> dict:
        return load_files(self.get_image_assets_path(app_name), Extension.HTML)

    def __init__(self, custom_executable_path: str = None):
        self.platform = get_os_platform()
        self._on_windows: bool = self.platform == OsPlatforms.WINDOWS
        self.platform_name: str = self.platform.value
        self.custom_executable_path: str = custom_executable_path
