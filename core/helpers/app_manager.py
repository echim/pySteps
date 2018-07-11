import os
import subprocess

from core.default_settings import DefaultSettings
from core.enums.os_platform import OsPlatform
from core.helpers.app_details import AppDetails
from core.helpers.os_helpers import get_app_full_name
from core.helpers.os_helpers import get_os_platform
from core.image_search.screen import Screen
from core.keyboard_commands.keyboard_commands import maximize_current_window, close_current_window


class AppManager:

    def __init__(self, app_details: AppDetails):

        self._app_details: AppDetails = app_details
        self._img_assets: dict = self._app_details.get_image_assets()

    @property
    def app_name(self):
        return self._app_details.app_name

    @property
    def app_path(self):
        return self._app_details.app_path

    def get_image_assets(self) -> dict:
        if self._img_assets is not None:
            return self._img_assets
        else:
            raise Exception('Unable to retrieve Image Assets')

    def launch_app(self, extra_params: str = None):
        launch_cmd = [self._app_details.app_path]
        if extra_params is not None and isinstance(extra_params, str):
            launch_cmd.append(extra_params)
        subprocess.Popen(launch_cmd, shell=False)

        Screen.image_wait(DefaultSettings.CONFIRM_LAUNCH_NAME.value, wait_seconds=10.0)
        maximize_current_window()

    def close_app(self):
        close_current_window()

        app_full_name = get_app_full_name(self.app_name)
        current_platform = get_os_platform()
        if current_platform == OsPlatform.WINDOWS:
            os.system('taskkill /f /im  %s' % app_full_name)
