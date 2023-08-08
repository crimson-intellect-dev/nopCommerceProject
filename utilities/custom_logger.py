import logging


class LogGenerator:
    @staticmethod
    def log_generator():
        logging.basicConfig(filename="./logs/automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
