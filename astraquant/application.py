from astraquant.startup import Startup
from astraquant.utils import LoggerFactory


class Application:

    @staticmethod
    def start() -> None:

        config = Startup.validate()

        logger = LoggerFactory.get_logger(
            level=config["logging"]["level"],
            log_file=config["logging"]["file"],
        )

        logger.info("Application Started")

        print("=" * 60)
        print(
            f"{config['application']['name']} "
            f"{config['application']['version']}"
        )
        print("=" * 60)

        logger.info("Startup validation completed successfully.")