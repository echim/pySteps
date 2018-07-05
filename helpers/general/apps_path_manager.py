from helpers.general.os_helpers import WinDefaultPaths, OsPlatforms, get_os


class AppsPathManager:

    def _init_app_paths(self) -> list:
        app_paths = []
        if self.platform == OsPlatforms.WINDOWS:
            app_paths.append(WinDefaultPaths.P_FILES_86.value)
            app_paths.append(WinDefaultPaths.P_FILES_64.value)
        elif self.platform == OsPlatforms.LINUX:
            raise Exception('Not Implemented')
        elif self.platform == OsPlatforms.OSX:
            raise Exception('Not Implemented')
        else:
            raise Exception('Unknown app paths for %s platform' % self.platform.value)

        return app_paths

    def __init__(self, custom_path: str or None = None):
        self.platform = get_os()
        self.platform_name: str = self.platform.value
        self.app_paths: list = self._init_app_paths() if custom_path is None else [custom_path]
