from core.image_search.image_search import find, find_all


class Screen:
    @staticmethod
    def find(asset_name: str):
        return find(asset_name)

    @staticmethod
    def find_all(asset_name: str):
        return find_all(asset_name)
