import os
import subprocess

from core.helpers.os_helpers import get_app_full_name, is_platform_windows
from core.helpers.path_manager import PathManager


class AppManager:

    def __init__(self, app_name: str, custom_executable_path: str = None):
        self._app_name: str = get_app_full_name(app_name)
        self._app_path: str = None
        self._img_assets: dict = None

        self._path_manager: PathManager = PathManager(custom_executable_path)
        self.sync_assets(self.app_name)

    def sync_assets(self, app_name):
        self._app_path: str = self._path_manager.get_app_path(app_name)
        self._img_assets: dict = self._path_manager.get_img_assets(app_name)

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, new_name: str):
        self._app_name = get_app_full_name(new_name)
        self.sync_assets(self._app_name)

    def get_image_assets(self) -> dict:
        if self._img_assets is not None:
            return self._img_assets
        else:
            raise Exception('Unable to retrieve Image Assets')

    def launch_app(self, extra_params: str = None):
        launch_cmd = [self._app_path]
        if extra_params is not None and isinstance(extra_params, str):
            launch_cmd.append(extra_params)
        subprocess.Popen(launch_cmd, shell=False)

    def close_app(self):
        app_full_name = get_app_full_name(self.app_name)
        if is_platform_windows():
            os.system('Taskkill /f /im %s' % app_full_name)
        else:
            raise Exception('Not implemented')
