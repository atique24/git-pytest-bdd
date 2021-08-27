import datetime
import logging
import inspect
import os


def custom_logger(loglevel=logging.INFO):

    filename = "automation.log"
    logDirectory = "..//logs//automation logs//" + str(datetime.date.today()) + "//"
    relativeFilename = logDirectory + filename
    currentDirectory = os.path.dirname(__file__)
    destinationPath = os.path.join(currentDirectory, relativeFilename)
    destinationFolder = os.path.join(currentDirectory, logDirectory)
    if not os.path.exists(destinationFolder):
        os.makedirs(destinationFolder)


    loggername = inspect.stack()[1][3]

    logger = logging.getLogger(loggername)
    logger.setLevel(loglevel)

    filehander = logging.FileHandler(filename=destinationPath, mode="a")
    filehander.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%d:%m:%y %H:%M:%S')
    filehander.setFormatter(formatter)

    logger.addHandler(filehander)

    return logger
