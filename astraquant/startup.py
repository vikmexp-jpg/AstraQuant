"""
Application startup validation.
"""

from astraquant.config import ConfigLoader, ConfigurationError


class Startup:

    @staticmethod
    def validate() -> dict:
        """
        Validate startup configuration.
        """

        config = ConfigLoader.load()

        required_sections = [
            "application",
            "environment",
            "market",
            "strategy",
            "logging",
        ]

        for section in required_sections:
            if section not in config:
                raise ConfigurationError(
                    f"Missing configuration section: {section}"
                )

        return config