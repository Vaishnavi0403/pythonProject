import inspect
import logging


class BaseClass:
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        if not logger.handlers:
            # create the handlers and call logger.addHandler(logging_handler)
            logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.warning("Something is in warning mode")
        # logger.error("A Major error has happend")
        # logger.critical("Critical issue")
