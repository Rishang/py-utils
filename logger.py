from logging import getLogger, StreamHandler, Formatter, INFO, DEBUG
from rich.logging import RichHandler

"""
This module is used to create a logger object that can be used to log messages to the console.
"""


# Create a logger object
class Logger:
    def __init__(self, name: str, level: int = DEBUG, set_name: bool = False):
        self.logger = getLogger(name)
        self.logger.setLevel(level)
        handler = RichHandler(log_time_format="%X", rich_tracebacks=True)
        handler.setLevel(level)
        if set_name:
            formatter = Formatter("%(name)s: %(message)s")
        else:
            formatter = Formatter("%(message)s")
        handler.setFormatter(formatter)
        handler.formatter = formatter
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)


# Create a logger object
log = Logger("log", level=INFO).get_logger()
