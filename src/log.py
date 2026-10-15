import logging

from config import CONFIG

LOG_DIR = CONFIG.paths.logs
LOG_DIR.mkdir(exist_ok=True)
FORMAT = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%H:%M:%S")


def log(name: str, level: int = logging.DEBUG):
    logger = logging.getLogger(name)
    if not logger.handlers:
        fhandler = logging.FileHandler(f"{LOG_DIR}/{name}.log", encoding="utf-8")
        fhandler.setFormatter(FORMAT)
        logger.addHandler(fhandler)
    return logger
