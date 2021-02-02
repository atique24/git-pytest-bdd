from base.base_page import BasePage
from utilities.customlogger import custom_logger
import logging
from utilities.util import Utilities
from selenium import webdriver





class MobilePage(BasePage):
    cl = custom_logger(logging.INFO)

    def __init__(self,driver):
        super(MobilePage, self).__init__(driver)
        self.driver = driver
        self.utill = Utilities()


    #locator
    _mobile = "MOBILE"
    _Iphone = "IPHONE"
    _samsung = "SAMSUNG GALAXY"
    _sony = "SONY XPERIA"
    _expected_list1 = ['IPHONE', 'SAMSUNG GALAXY', 'SONY XPERIA']
    _expected_list2 = ['SONY XPERIA', 'SAMSUNG GALAXY', 'IPHONE']
    _tv = "TV"
    _grid_view = "//strong[@title='Grid']"
    _list_view = "List"
    _value = "//span[@id='product-price-1']/child::span"
    _add_to_cart = "//a[@title='Xperia']//following-sibling::div//span[text()='Add to Cart']"
    _cart_quantity = "//input[@data-cart-item-id='MOB001' and @title='Qty']"
    _update = "//button[@title='Update']/span/span"
    _error = "//span[text()='Some of the products cannot be ordered in requested quantity.']"
    _compare_add_product = "//a[text()='Sony Xperia']/parent::h2/parent::div/child::div/child::ul/li/a[text()='Add to Compare']"
    _compare_button = "//span[text()='Compare']"
    _compare_screen = "//h1[text()='Compare Products']"
    _iphone_new = "//a[text()='IPhone']"
    _close_window = "//span[text()='Close Window']"
    _available_mobile = "//div[@class='category-products']/ul/li/a"
    _mobile_text = "//li[@class='item last']//child::div/h2/a"
    _sort_by = "//select[@title='Sort By']"


    def mobile_tab(self):
        self.elementClick(self._mobile,"link")

    def available_mobiles(self,expected_list):
        result = self.getAttributelist(self._available_mobile,'xpath','title')
        return self.utill.listcompare(result,expected_list)

    def sort_by(self,visibleText):
        self.get_element_dropdown_value(self._sort_by,'xpath',selectType='text',value=visibleText)

    def get_mobile_text(self):
        return self.getTextElementList(self._mobile_text,'xpath')

    def verify_sort_functionality(self,result):
        result1 = self.get_mobile_text()
        res = result.strip('][').split(', ')
        print(res)
        return self.utill.listcompare(expectedList=res,actualList=result1)

    def add_to_cart(self):
        self.elementClick(self._add_to_cart,'xpath')

    def enter_cart_quantity_and_update(self):
        self.elementSend(self._cart_quantity,'xpath','1000')
        self.explicitwait(self._update,'xpath',20,0.1)
        self.elementClick(self._update,'xpath')
        return self.isElementDisplayed(self._error,'xpath')


    def click_tv_tab(self):
        self.elementClick(self._tv,'link')
        print('clicked on Tv')


    def click_list_view(self):
        self.elementClick(self._list_view,'link')


    def sony_price_grid_view(self):
        value1 = self.getText(self._value,'xpath')
        return value1

    def sony_price_list_view(self):
        value2 = self.getText(self._value,'xpath')
        return value2


    def add_product1_for_compare(self,mobile1):
        compare = f"//a[text()='{mobile1}']/parent::h2/parent::div/child::div/child::ul/li/a[text()='Add to Compare']"
        self.elementClick(compare,'xpath')

    def add_product2_for_compare(self,mobile2):
        compare = f"//a[text()='{mobile2}']/parent::h2/parent::div/child::div/child::ul/li/a[text()='Add to Compare']"
        self.elementClick(compare,'xpath')

    def click_compare_button(self):
        self.elementClick(self._compare_button,'xpath')

    def confirm_compare_window(self):
        self.switching_to_window()
        return self.isElementDisplayed(self._compare_screen,'xpath')









