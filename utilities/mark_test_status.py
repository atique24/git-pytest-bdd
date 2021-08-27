from utilities.customlogger import custom_logger
import logging
from base.SeleniumBase import SeleniumBase



class MarkTestStatus(SeleniumBase):
    cl = custom_logger(logging.INFO)
    def __init__(self,driver):
        super(MarkTestStatus, self).__init__(driver)
        self.driver = driver

        self.resultlist=[]

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result is True:
                    self.resultlist.append("Pass")
                    self.cl.info("###Verification Successfull :: + " + resultMessage)
                else:
                    self.resultlist.append("Fail")
                    self.cl.info("###Verification Failed :: + " + resultMessage)
                    self.savescreenshots(resultMessage)

            else:
                self.resultlist.append("Fail")
                self.cl.info("###Verification Failed :: + " + resultMessage)

        except:
            self.resultlist.append("Fail")
            self.savescreenshots(resultMessage)
            self.cl.info("### Exception Occured !!!")


    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)


    def finalMark(self,testcase,result,resultMessage):
        self.setResult(result, resultMessage)

        if "Fail" in self.resultlist:
            self.cl.info(testcase + "### Test Failed")
            self.resultlist.clear()
            assert True == False

        else:
            self.cl.info(testcase + "### Test Passed")
            self.resultlist.clear()
            assert True == True




