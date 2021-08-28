from selenium.webdriver.common.by import By

from base.SeleniumBase import SeleniumBase
from base.base_page import BasePage
from utilities.customlogger import custom_logger
import logging
from utilities.util import Utilities
from selenium import webdriver





class MobilePage(SeleniumBase):
    cl = custom_logger(logging.INFO)

    def __init__(self,driver):
        super(MobilePage, self).__init__(driver)
        self.driver = driver
        self.utill = Utilities()


    #locator
    _mobile = (By.LINK_TEXT,"MOBILE")
    _Iphone = "IPHONE"
    _samsung = "SAMSUNG GALAXY"
    _sony = "SONY XPERIA"
    _expected_list1 = ['IPHONE', 'SAMSUNG GALAXY', 'SONY XPERIA']
    _expected_list2 = ['SONY XPERIA', 'SAMSUNG GALAXY', 'IPHONE']
    _tv = (By.LINK_TEXT,"TV")
    _grid_view = "//strong[@title='Grid']"
    _list_view = (By.LINK_TEXT,"List")
    _value = (By.XPATH,"//span[@id='product-price-1']/child::span")
    _add_to_cart = (By.XPATH,"//a[@title='Xperia']//following-sibling::div//span[text()='Add to Cart']")
    _cart_quantity = (By.XPATH,"//input[@data-cart-item-id='MOB001' and @title='Qty']")
    _update = (By.XPATH, "//button[@title='Update']/span/span")
    _error = (By.XPATH,"//span[text()='Some of the products cannot be ordered in requested quantity.']")
    _compare_add_product = "//a[text()='Sony Xperia']/parent::h2/parent::div/child::div/child::ul/li/a[text()='Add to Compare']"
    _compare_button = (By.XPATH, "//span[text()='Compare']")
    _compare_screen = (By.XPATH,"//h1[text()='Compare Products']")
    _iphone_new = "//a[text()='IPhone']"
    _close_window = "//span[text()='Close Window']"
    _available_mobile = (By.XPATH,"//div[@class='category-products']/ul/li/a")
    _mobile_text = (By.XPATH, "//li[@class='item last']//child::div/h2/a")
    _sort_by = (By.XPATH,"//select[@title='Sort By']")


    def mobile_tab(self):
        self.elementClick(self._mobile)

    def available_mobiles(self):
        return self.getAttributeList(self._available_mobile,attributeType= 'title')



    def sort_by(self,visibleText):
        self.selectByVisibleText(self._sort_by, visibleText)


    def get_mobile_text(self):
        return self.getElementsText(self._mobile_text)

    def verify_sort_functionality(self,result):
        result1 = self.get_mobile_text()
        res = result.strip('][').split(', ')
        return result1 == res

    def add_to_cart(self):
        self.elementClick(self._add_to_cart)

    def enter_cart_quantity_and_update(self):
        self.elementSend(self._cart_quantity,'1000')
        #self.explicitwait(self._update,'xpath',20,0.1)
        self.elementClick(self._update)
        return self.isElementDisplayed(self._error)


    def click_tv_tab(self):
        self.elementClick(self._tv)
        print('clicked on Tv')


    def click_list_view(self):
        self.elementClick(self._list_view)


    def sony_price_grid_view(self):
        return self.getElementText(self._value)


    def sony_price_list_view(self):
        return self.getElementText(self._value)



    def add_product1_for_compare(self,mobile1):
        compare = (By.XPATH, f"//a[text()='{mobile1}']/parent::h2/parent::div/child::div/child::ul/li/a[text()='Add to Compare']")
        self.elementClick(compare)

    def add_product2_for_compare(self,mobile2):
        compare = (By.XPATH, f"//a[text()='{mobile2}']/parent::h2/parent::div/child::div/child::ul/li/a[text()='Add to Compare']")
        self.elementClick(compare)

    def click_compare_button(self):
        self.elementClick(self._compare_button)

    def confirm_compare_window(self):
        self.switchWindow(1)
        return self.isElementDisplayed(self._compare_screen)









