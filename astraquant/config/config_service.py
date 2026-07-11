from .config_loader import ConfigLoader


class ConfigService:
    _config = None

    @classmethod
    def get(cls):
        if cls._config is None:
            cls._config = ConfigLoader.load()
        return cls._config