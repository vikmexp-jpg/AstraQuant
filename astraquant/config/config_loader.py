from pathlib import Path

import yaml

from .exceptions import ConfigurationError


class ConfigLoader:
    """Loads application configuration."""

    CONFIG_FILE = Path("config") / "config.yaml"

    @classmethod
    def load(cls) -> dict:
        """Load configuration from YAML."""

        if not cls.CONFIG_FILE.exists():
            raise ConfigurationError(
                f"Configuration file not found: {cls.CONFIG_FILE}"
            )

        with cls.CONFIG_FILE.open("r", encoding="utf-8") as stream:
            config = yaml.safe_load(stream)

        if not isinstance(config, dict):
            raise ConfigurationError("Invalid configuration format.")

        return config