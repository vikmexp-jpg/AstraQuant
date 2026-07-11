from astraquant.application import Application
from astraquant.config import ConfigLoader


def main() -> None:
    config = ConfigLoader.load()

    Application.start()

    print()
    print("Configuration Loaded Successfully")
    print(f"Mode      : {config['environment']['mode']}")
    print(f"Market    : {config['market']['symbol']}")
    print(f"Strategy  : {config['strategy']['name']}")


if __name__ == "__main__":
    main()