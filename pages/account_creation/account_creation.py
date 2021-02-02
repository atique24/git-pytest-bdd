from base.selenium_driver import SeleniumDriver
from utilities.customlogger import custom_logger
import logging
import time
from pages.mobile_page.mobile_page import MobilePage


class Account(SeleniumDriver):
    cl = custom_logger(loglevel=logging.INFO)

    def __init__(self,driver):
        super(Account, self).__init__(driver)
        self.driver = driver
        self.mb = MobilePage(self.driver)


    #locators
    _account = "//a/span[text()='Account']"
    _register = "Register"
    _firstname = "firstname"
    _lastname = "lastname"
    _email_address = "email_address"
    _password = "password"
    _confirmation = "confirmation"
    _checkbox = "is_subscribed"
    _registeration= "//button[@title='Register']"

    _tv = "TV"
    _add_to_wishlist = "//a[@title='LG LCD']//following-sibling::div/child::div/ul/li/a"
    _share_wishlist = "//span[text()='Share Wishlist']"
    _emailaddress_wishlist = "email_address"
    _message_wishlist = "message"
    _message_success_sharelist = "//span[text()='Your Wishlist has been shared.']"



    def click_account(self):
        self.elementClick(self._account, 'xpath')
        self.elementClick(self._register, 'link')

    def fill_registration(self,firstName,lastName,emailAddress,password,confirmPassword):
        self.elementSend(self._firstname, 'id', firstName)
        self.elementSend(self._lastname, 'id', lastName)
        self.elementSend(self._email_address, 'id', emailAddress)
        self.elementSend(self._password, 'id', password)
        self.elementSend(self._confirmation, 'id', confirmPassword)

    def checkbox(self,):
        self.elementClick(self._checkbox, 'id')

    def click_registration_button(self):
        self.elementClick(self._registeration,'xpath')


    def success_message(self,success):
        _success_message = f"//span[text()='{success}']"
        return self.isElementDisplayed(_success_message,'xpath')











