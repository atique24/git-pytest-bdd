from base.SeleniumBase import SeleniumBase
from utilities.util import Utilities


class BasePage(SeleniumBase):
    def __init__(self,driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Utilities()


    def verify_page_title(self, titleToVerify):
        actualTitle = self.getTitle()
        return self.util.verify_text_contains(actualText = actualTitle, expectedText=titleToVerify)
