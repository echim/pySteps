from core.enums.app_name import AppName
from core.enums.custom_paths import CustomPaths
from core.helpers.os_helpers import get_os_platform, OsPlatform
from core.helpers.path_manager import PathManager, get_app_full_name, get_app_base_name


class AppDetails:
    def __init__(self, app_name: AppName, with_custom_path: bool = False):
        custom_path: str = None
        if with_custom_path:
            os_platform: OsPlatform = get_os_platform()
            custom_path = CustomPaths[os_platform.name].value[app_name.name]

        self._path_manager: PathManager = PathManager(custom_path)
        self._app_name = get_app_base_name(app_name.value)
        self._app_full_name = get_app_full_name(app_name.value)

    @property
    def app_name(self):
        return self._app_name

    @property
    def full_name(self):
        return self._app_full_name

    @property
    def app_path(self):
        return self._path_manager.find_app_path_by_name(self._app_name)

    def get_image_assets(self):
        return self._path_manager.get_img_assets(self._app_name)
