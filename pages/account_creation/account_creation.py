from selenium.webdriver.common.by import By

from base.SeleniumBase import  SeleniumBase
from utilities.customlogger import custom_logger
import logging
import time
from pages.mobile_page.mobile_page import MobilePage


class Account(SeleniumBase):
    cl = custom_logger(loglevel=logging.INFO)

    def __init__(self,driver):
        super(Account, self).__init__(driver)
        self.driver = driver
        self.mb = MobilePage(self.driver)


    #locators
    _account = (By.XPATH, "//a/span[text()='Account']")
    _register = (By.LINK_TEXT,"Register")
    _firstname = (By.ID,"firstname")
    _lastname = (By.ID,"lastname")
    _email_address = (By.ID,"email_address")
    _password = (By.ID,"password")
    _confirmation = (By.ID,"confirmation")
    _checkbox = (By.ID, "is_subscribed")
    _registeration= (By.XPATH,"//button[@title='Register']")

    _tv = "TV"
    _add_to_wishlist = "//a[@title='LG LCD']//following-sibling::div/child::div/ul/li/a"
    _share_wishlist = "//span[text()='Share Wishlist']"
    _emailaddress_wishlist = "email_address"
    _message_wishlist = "message"
    _message_success_sharelist = "//span[text()='Your Wishlist has been shared.']"



    def click_account(self):
        self.elementClick(self._account)
        self.elementClick(self._register)

    def fill_registration(self,firstName,lastName,emailAddress,password,confirmPassword):
        self.elementSend(self._firstname, firstName)
        self.elementSend(self._lastname, lastName)
        self.elementSend(self._email_address, emailAddress)
        self.elementSend(self._password, password)
        self.elementSend(self._confirmation, confirmPassword)

    def checkbox(self,):
        self.elementClick(self._checkbox)

    def click_registration_button(self):
        self.elementClick(self._registeration)


    def success_message(self,success):
        _success_message = (By.XPATH,f"//span[text()='{success}']")
        return self.isElementDisplayed(_success_message)











