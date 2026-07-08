from astraquant.config.loader import load_config
from astraquant.utils.logger import get_logger

cfg = load_config()
log = get_logger()

log.info("Starting AstraQuant")
print(cfg)
