import os
import subprocess

from core.default_settings import DefaultSettings
from core.helpers.app_details import AppDetails
from core.helpers.os_helpers import get_app_full_name
from core.helpers.os_helpers import platform_is_linux, platform_is_windows, platform_is_darwin
from core.helpers.webdriver_helpers import get_webdriver_by_app_name
from core.keyboard_commands.keyboard_commands import maximize_current_window, close_current_window
from core.screen.screen import Screen


class AppManager:

    def __init__(self, app_details: AppDetails, with_web_driver: bool = False):

        self._app_details: AppDetails = app_details
        self._img_assets: dict = self._app_details.get_image_assets()
        self._driver = with_web_driver
        self.browser = None

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

        if self._driver:
            self.browser = get_webdriver_by_app_name(self.app_name)
            Screen.image_wait(DefaultSettings.CONFIRM_LAUNCH_NAME.value, wait_seconds=10.0)
            self.browser.maximize_window()
        else:
            launch_cmd = [self._app_details.app_path]
            if extra_params is not None and isinstance(extra_params, str):
                launch_cmd.append(extra_params)

            if platform_is_darwin():
                launch_cmd = "open -a %s --args %s" % (self._app_details.app_name, extra_params)

            subprocess.Popen(launch_cmd, shell=True)

            Screen.image_wait(DefaultSettings.CONFIRM_LAUNCH_NAME.value, wait_seconds=10.0)
            maximize_current_window()

    def close_app(self):
        if self._driver:
            self.browser.quit()
        else:
            close_current_window()

            app_full_name = get_app_full_name(self.app_name)
            if platform_is_windows():
                os.system('taskkill /f /im  %s' % app_full_name)
            elif platform_is_linux():
                os.system('pkill %s' % app_full_name)
            elif platform_is_darwin():
                os.system('killall %s' % app_full_name)
