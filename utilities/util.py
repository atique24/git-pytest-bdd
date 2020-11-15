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


    def verify_text_contains(self,actualText, expectedText):
        self.cl.info("Actual text from application URL is :: " + str(actualText))
        self.cl.info("Expected text from application URL is :: " + str(expectedText))

        if actualText.lower() in expectedText.lower():
            self.cl.info("### Verfication Passed !!!")
            return True
        else:
            self.cl.info("### Verfication Failed !!!")
            return False


    def verify_text(self,actualText, expectedText):
        self.cl.info("Actual text from application URL is :: " + str(actualText))
        self.cl.info("Expected text from application URL is :: " + str(expectedText))

        if actualText.lower() == expectedText.lower():
            self.cl.info("### Verfication Passed")
            return True
        else:
            self.cl.log.info("### Verfication Failed")
            return False

    def getAlphaNumeric(self,length,type):

        alpha_num = ""

        if type == "lower":
            value = string.ascii_lowercase

        elif type == "upper":
            value = string.ascii_uppercase

        elif type == "digits":
            value = string.digits

        elif type == "mix":
            value = string.ascii_letters + string.digits

        elif type == "letters":
            value = string.ascii_letters

        for i in range(0,length):
            return alpha_num.join(random.choice(value))


    def listcompare(self,expectedList, actualList):
        try:
            self.cl.info("Expected List is :: " + str(expectedList))
            self.cl.info("Actual List is :: " + str(actualList))

            if len(expectedList) == len(actualList):
                i = 0
                for i in range(0, len(actualList)):
                    if expectedList[i] == actualList[i]:
                        i = i + 1
                        if i == len(actualList):
                            return True
                            self.log.info("Both List Matched")

                    else:
                        return False
                        self.log.info("List Does not match")
                        break
            else:
                print("List Length does not match")
                return False

        except:
            print("List Length does not match")
            return False


    def verify_values(self,expectedValue,ActualValue):
        try:
            if expectedValue == ActualValue:
                self.cl.info("Matched")
                return True
            else:
                self.cl.info("Values dont match")
                return False
        except:
            self.cl.info("Exception occured.. Values dont match")
            return False







