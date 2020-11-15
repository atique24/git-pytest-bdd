import logging
import inspect

def custom_logger(loglevel = logging.INFO):
    loggername = inspect.stack()[1][3]

    logger = logging.getLogger(loggername)
    logger.setLevel(loglevel)

    filehander = logging.FileHandler(filename="Automation.log" , mode="a")
    filehander.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%d:%m:%y %H:%M:%S')
    filehander.setFormatter(formatter)


    logger.addHandler(filehander)

    return logger
