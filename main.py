from astraquant.application import Application
from astraquant.config import ConfigurationError


def main() -> None:
    try:
        Application.start()

    except ConfigurationError as error:
        print(f"[CONFIGURATION ERROR] {error}")

    except Exception as error:
        print(f"[UNEXPECTED ERROR] {error}")
        raise


if __name__ == "__main__":
    main()