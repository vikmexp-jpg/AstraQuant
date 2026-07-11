"""
Application entry point for AstraQuant.
"""

from astraquant.version import APPLICATION_NAME, VERSION


class Application:
    """Main application."""

    @staticmethod
    def start() -> None:
        print("=" * 60)
        print(f"{APPLICATION_NAME} {VERSION}")
        print("=" * 60)
        print("Application initialized successfully.")