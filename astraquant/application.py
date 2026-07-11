from astraquant.config import ConfigLoader
from astraquant.utils import LoggerFactory


class Application:

    @staticmethod
    def start() -> None:

        config = ConfigLoader.load()

        logger = LoggerFactory.get_logger(
            level=config["logging"]["level"],
            log_file=config["logging"]["file"],
        )

        logger.info("Application Started")

        logger.info(
            "Mode=%s Market=%s Strategy=%s",
            config["environment"]["mode"],
            config["market"]["symbol"],
            config["strategy"]["name"],
        )

        print("=" * 60)
        print(
            f"{config['application']['name']} "
            f"{config['application']['version']}"
        )
        print("=" * 60)