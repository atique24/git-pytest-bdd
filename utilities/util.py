import datetime

from utilities.customlogger import custom_logger
import time
import random
import string
import logging
from traceback import print_stack

class Utilities():
    cl = custom_logger(logging.INFO)

    def sleep(self,sec,info =""):
        if info is not None:
            self.cl.info("Wait :: " +str(sec) + " seconds for " + str(info) )
        try:
            time.sleep(sec)
        except InterruptedError:
            self.cl.error("Exception occured while Sleep")





    def generate_date_time(self):
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H-%M-%S-%f')







