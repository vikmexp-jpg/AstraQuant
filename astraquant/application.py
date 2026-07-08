from astraquant.config.config_loader import ConfigLoader
from astraquant.constants import APP_NAME
from astraquant.utils.logger import get_logger

class Application:
    def __init__(self):
        self.logger=get_logger(APP_NAME)
        self.config=ConfigLoader.load()

    def start(self):
        self.logger.info("Application Started")
        self.logger.info("Strategy : %s", self.config["strategy"]["active"])
        self.logger.info("Market : %s", self.config["market"]["symbol"])
