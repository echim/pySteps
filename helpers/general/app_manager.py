from helpers.general.os_helpers import load_files, get_os, OsPlatforms, Extensions
from helpers.general.apps_path_manager import AppsPathManager
import subprocess


class AppManager:

    def __init__(self, app_name: str, custom_path: str or None = None):
        self._app_name: str = app_name
        self._app_exists: bool = False
        self._app_path: str = None
        self._on_windows: bool = get_os() == OsPlatforms.WINDOWS

        self._path_manager: AppsPathManager = AppsPathManager(custom_path)
        self._apps: dict = self._load_all_apps()
        self._check_app_exists()

    def _load_all_apps(self):
        extension = Extensions.EXE.value if self._on_windows else None
        return load_files(self._path_manager.app_paths, extension)

    def _check_app_exists(self):
        if self._on_windows:
            self._app_name = self._app_name + Extensions.EXE.value

        if self._app_name in self._apps.keys():
            self._app_exists = True
            self._app_path = self._apps[self._app_name]
        else:
            raise Exception('Unable to find %s in %s' % (self._app_name, self._path_manager.app_paths))

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, new_name: str):
        self._app_name = new_name
        self._check_app_exists()

    def launch_app(self):
        if self._app_exists:
            process = subprocess.Popen([self._app_path])
