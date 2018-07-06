from helpers.general.apps_path_manager import PathManager
import subprocess


class AppManager:

    def __init__(self, app_name: str, custom_executable_path: str = None):
        self._app_name: str = app_name
        self._app_path: str = None
        self._img_assets: dict = None

        self._path_manager: PathManager = PathManager(custom_executable_path)
        self.sync_assets(app_name)

    def sync_assets(self, app_name):
        self._app_path: str = self._path_manager.get_app_path(app_name)
        self._img_assets: dict = self._path_manager.get_img_assets(app_name)

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, new_name: str):
        self._app_name = new_name
        self.sync_assets(new_name)

    def get_image_assets(self) -> dict:
        if self._img_assets is not None:
            return self._img_assets
        else:
            raise Exception('Unable to retrieve Image Assets')

    def launch_app(self):
        process = subprocess.Popen([self._app_path])
