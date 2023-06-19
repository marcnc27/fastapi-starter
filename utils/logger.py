import logging

from constants import app_title

logging.basicConfig(format=f'%(asctime)s - [{app_title}] - %(levelname)s: %(name)s - %(message)s')


class Logger:

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name=name)
        logger.setLevel(level=logging.DEBUG)
        return logger
