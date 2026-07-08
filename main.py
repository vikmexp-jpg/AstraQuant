from astraquant.config.config_loader import ConfigLoader
from astraquant.constants import APP_NAME, APP_VERSION
from astraquant.utils.logger import get_logger


def banner():

    print("=" * 60)
    print(f"{APP_NAME} {APP_VERSION}")
    print("=" * 60)


def main():

    banner()

    logger = get_logger(APP_NAME)

    config = ConfigLoader.load()

    logger.info("Application Started")

    logger.info(
        f"Strategy : {config['strategy']['active']}"
    )

    logger.info(
        f"Market : {config['market']['symbol']}"
    )


if __name__ == "__main__":

    main()