import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(os.path.abspath(os.curdir) + "//logs//automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
