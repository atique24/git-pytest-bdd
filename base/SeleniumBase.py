import datetime
import time

import requests
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from utilities.customlogger import custom_logger
import logging
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from traceback import #print_stack()
from selenium.webdriver.support.color import Color
from utilities.util import Utilities


class SeleniumBase():
    enableScreenshot = False
    cl = custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.util = Utilities()

    @classmethod
    def EnableScreenshotForTest(cls, screenshot):
        cls.enableScreenshot = screenshot

    """
    Below method is deprecated
    """

    # def ByType(self, locatorType):
    #     locatorType = locatorType.lower()
    #
    #     if locatorType == "id":
    #         return By.ID
    #     elif locatorType == "xpath":
    #         return By.XPATH
    #     elif locatorType == "css":
    #         return By.CSS_SELECTOR
    #     elif locatorType == "link":
    #         return By.LINK_TEXT
    #     elif locatorType == "partial link":
    #         return By.PARTIAL_LINK_TEXT
    #     elif locatorType == "name":
    #         return By.NAME
    #     elif locatorType == "tag":
    #         return By.TAG_NAME
    #     elif locatorType == "class":
    #         return By.CLASS_NAME
    #
    #     else:
    #         self.cl.info("Invalid Locatortype " + str(locatorType))

    def visit(self, url):
        try:
            self.driver.get(url)
            element = self.driver.find_elements(By.TAG_NAME, 'title')
            self.cl.info("The element list is :: " + str(element))
            if len(element) == 0:
                i = 0
                while i < 5:
                    if len(element) == 0:
                        i += 1
                        time.sleep(2)
                        self.cl.info("Website is not loaded. Reloading the website for :: " + str(i) + 'st time')
                        self.driver.get(url)
                        element = self.driver.find_elements(By.TAG_NAME, 'title')

                    else:
                        self.cl.info("The element list is :: " + str(element))
                        break
            else:
                self.cl.info("Website is loaded.")
        except Exception as e:
            self.cl.error("Unable to open URL from :: " + str(url) + '. ' + "Exception Occurred :: " + str(
                e.__class__.__name__))


    # def visit(self, url):
    #     try:
    #         i = 0
    #         while i < 5:
    #             self.driver.get(url)
    #             element = self.driver.find_elements(By.TAG_NAME, 'title')
    #             self.cl.info("The element list is :: " + str(element))
    #             if len(element) < 1:
    #                 i += 1
    #                 time.sleep(2)
    #                 self.cl.info("Website is not loaded. Reloading the website for :: " + str(i) + 'st time')
    #                 self.driver.get(url)
    #
    #             else:
    #                 self.cl.info("Website is loaded.")
    #                 break
    #     except Exception as e:
    #         self.cl.error("Unable to open URL from :: " + str(url) + '. ' + "Exception Occurred :: " + str(
    #             e.__class__.__name__))

    def findElement(self, locator, timeout=5, poll_frequency=0):
        element = None

        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            self.cl.info(
                "Waiting for " + str(timeout) + " seconds to find the element for locator :: " + str(
                    locator))
            element = wait.until(ec.presence_of_element_located(locator))
            self.cl.info(
                "Element :: " + str(element.id) + " found for locator :: " + str(locator) + ". Session_id :: " + str(
                    element.parent.session_id))

            # element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
            # if self.enableScreenshot:
            #     self.saveScreenshots()

        except Exception as e:
            self.cl.error("No Element found for locator :: " + str(locator) + '. ' + "Exception Occurred :: " + str(
                e.__class__.__name__))
            # print_stack()()
        return element

    def findElements(self, locator):
        element = []
        try:
            element = self.driver.find_elements(*locator)
            if len(element) > 0:
                self.cl.info("Elements list returned::  " + str(element)  + " for locator :: " + str(locator))

            else:
                self.cl.info(
                    "Elements not found for locator :: " + str(locator) + ". Empty List returned " + str(element))

        except Exception as e:
            self.cl.error(
                "Element could not be found for :: " + str(locator) + '. ' + str(
                    e.__class__.__name__) + ' ' + str(e))
            # print_stack()()
        return element

    def selectByIndex(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                sel = Select(element)
                sel.select_by_index(value)
                self.cl.info("Selected element with index " + str(value) + " from the drop down using Index position")
                # if self.enableScreenshot:
                #     self.saveScreenshots()

            else:
                self.cl.error("Unable to select element by Index. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to select element by Index. Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def selectByVisibleText(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                # self.saveScreenshots()
            if element:
                sel = Select(element)
                sel.select_by_visible_text(value)
                self.cl.info("Selected element with value " + str(value) + " from the drop down using Visible Text")
                # if self.enableScreenshot:
                #     self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to select element by Visible Text. No element was found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Unable to select element by Visible Text. Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def selectByValue(self, locator, value, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                # self.saveScreenshots()
            if element:
                sel = Select(element)
                sel.select_by_value(value)
                self.cl.info("Selected element with Name " + str(value) + " from the drop down using Value")
                # if self.enableScreenshot:
                #     self.saveScreenshots()

            else:
                self.cl.error(
                    "Unable to select element by Visible Text. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to select element from the dropdown. Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def visibilityOfElementLocated(self, locator, timeout=10, poll_frequency=0.2):
        element = None
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            self.cl.info(
                "Waiting for " + str(timeout) + " seconds for checking the element visibility :: " + str(
                    locator))
            element = wait.until(ec.visibility_of_element_located(locator))

            self.cl.info(
                "Element :: " + str(element.id) + " is visible on page for locator :: " + str(
                    locator) + ". Session_id :: " + str(
                    element.parent.session_id))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
            if self.enableScreenshot:
                self.saveScreenshots()

        except Exception as e:
            self.cl.error("Unable to find element with locator :: " + str(locator) + '. Exception occurred ' + str(
                e.__class__.__name__) + str(e))
        return element

    def elementClick(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)

            if element:
                if self.enableScreenshot:
                    self.saveScreenshots()
                element.click()
                self.cl.info("Clicked on Element : " + str(element.id))
            else:
                self.cl.error("Unable to click on locator. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to click the element: " + str(locator) + ". Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def elementSend(self, locator, message, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                # if self.enableScreenshot:
                #     self.saveScreenshots()
                element.send_keys(message)
                self.cl.info("Text :: " + str(message) + " entered on element :: " + str(element.id))
                # if self.enableScreenshot:
                #     self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to send the message on the element. No Element found for the locator ::  " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to send the message on locator: " + str(locator) + "Exception :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            # print_stack()()

    def verifyExactTitle(self, expectedTitle, timeout=10, poll_frequency=0.2):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            result = wait.until(ec.title_is(expectedTitle))
            if result:
                self.cl.info("The actual title of the webpage is :: " + str(self.driver.title))
                self.cl.info("The expected title is :: " + str(expectedTitle))
                self.cl.info("Title Match")
            else:
                self.cl.info("Title doesnt match")

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current page title. Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            result = False
            # print_stack()()
        return result

    def verifyTitleContains(self, title, timeout=15, poll_frequency=0.2):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
            result = wait.until(ec.title_contains(title))
            if result:
                self.cl.info("'" + title + "'" + " is part of the page title :: " + str(self.driver.title))
            else:
                self.cl.info("Title of the page doesnt contain text :: " + title)

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current page title. Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            result = False
            # print_stack()()
        return result

    def getElementText(self, locator, element=None):
        element_text = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                element_text = element.text
                self.cl.info("Text of the element : " + str(locator) + " is " + element_text)
            else:
                self.cl.error(
                    "Unable to find the text for element. No Element found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to find the text for element : " + str(
                    locator) + ". Following Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(e))
            # print_stack()()

        return element_text

    def getElementsText(self, locator, elements=None):
        elementText = []
        try:
            if locator:
                elements = self.findElements(locator)
            if len(elements) > 0:
                for item in elements:
                    itemText = item.text
                    elementText.append(itemText)
                self.cl.info("The TEXT for Elements are :: " + str(elementText))

            else:
                self.cl.error(
                    "Unable to find text for the element list. No elements found for the locator :: " + str(locator))

        except Exception as e:
            self.cl.error("Unable to return text for elements. Following Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()
        return elementText

    def getAttribute(self, locator, attributeType, element=None):
        elementAttribute = None
        try:
            if locator:
                element = self.findElement(locator)

            if element:
                elementAttribute = element.get_attribute(attributeType)
                self.cl.info("Value of Attribute :: " + attributeType + " is " + str(elementAttribute))
            else:
                self.cl.error(
                    "Unable to get the value of attribute " + attributeType + ". No element was found for locator :: " + str(
                        locator))
        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(
                    e))
            # print_stack()()
        return elementAttribute

    def getAttributeList(self, locator, attributeType, elements=None):
        element_attribute = []

        try:
            if locator:
                elements = self.findElements(locator)
            if len(elements) > 0:
                for item in elements:
                    elementAttribute = item.get_attribute(attributeType)
                    element_attribute.append(elementAttribute)
                    self.cl.info("Value of attribute")
            self.cl.info("Attribute list is :: " + str(element_attribute))


        except Exception as e:
            self.cl.error("Unable to find the value of attribute for element : " + str(
                locator) + " exception :: " + str(e))
            #print_stack()()
        return element_attribute

    def getValueOfCssProperty(self, locator, attributeType, element=None):
        cssAttributeProperty = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                cssAttributeProperty = element.value_of_css_property(property_name=attributeType)
                self.cl.info("Value of CSS Attribute :: " + attributeType + " is " + cssAttributeProperty)
            # if attributeType == 'Color': formatted_name = Color.from_string(cssAttributeProperty).hex self.cl.info(
            # "Value of CSS Attribute :: " + attributeType + " in HEX format is " + cssAttributeProperty) return
            # formatted_name
            else:
                self.cl.error("Unable to find the value of css property for element. No element was found for the "
                              "locator :: " + str(locator))
        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following Exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(
                    e))
            # print_stack()()
        return cssAttributeProperty

    def waitToClickElement(self, locator, time=5, poll=0.2):
        element = None
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[ElementNotInteractableException, ElementNotVisibleException,
                                                     NoSuchElementException, TimeoutException,
                                                     StaleElementReferenceException, ElementClickInterceptedException])
            self.cl.info(
                "Waiting to click on element : " + str(locator) + "for time " + str(time) + "sec")
            element = wait.until(ec.element_to_be_clickable(locator))
            self.cl.info("Element is Available for action")

        except Exception as e:
            self.cl.error("Unable to find the element " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()
        return element

    def waitForIframe(self, locator, index=None, time=10, poll=0.5):
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchFrameException, NoSuchElementException, TimeoutException])
            self.cl.info("Waiting to find iframe with : " + str(locator) + "with index position:: " + str(
                index) + "for time " + str(
                time) + "sec")
            wait.until(
                ec.frame_to_be_available_and_switch_to_it(locator))
            self.cl.info("iFrame is Available for switching")

        except Exception as e:
            self.cl.error("Unable to find the iframe. Following Exception occurred " + '. ' + str(
                e.__class__.__name__) + str(e))

    def elementClear(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                if self.enableScreenshot:
                    self.saveScreenshots()

            if element:
                element.clear()
                self.cl.info("Cleared Element : " + str(element))
                if self.enableScreenshot:
                    self.saveScreenshots()
            else:
                self.cl.error("Unable to clear the element. No element found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Unable to clear element. Exception :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def full_screenshot_with_scroll(self, driver, save_path):
        from io import StringIO
        from io import BytesIO
        from PIL import Image

        # initiate value

        save_path = save_path
        img_li = []  # to store image fragment
        offset = 0  # where to start

        # js to get height
        height = self.driver.execute_script(
            "return Math.max(" "document.documentElement.clientHeight, window.innerHeight);")

        # js to get the maximum scroll height
        # Ref--> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
        max_window_height = self.driver.execute_script(
            "return Math.max("
            "document.body.scrollHeight, "
            "document.body.offsetHeight, "
            "document.documentElement.clientHeight, "
            "document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight);"
        )

        # looping from top to bottom, append to img list
        # Ref--> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
        while offset < max_window_height:
            # Scroll to height
            driver.execute_script(f"window.scrollTo(0, {offset});")
            img = Image.open(BytesIO((self.driver.get_screenshot_as_png())))
            img_li.append(img)
            offset += height

        # In case it is not a perfect fit, the last image contains extra at the top.
        # Crop the screenshot at the top of last image.
        extra_height = offset - max_window_height
        if extra_height > 0 and len(img_li) > 1:
            pixel_ratio = driver.execute_script("return window.devicePixelRatio;")
            extra_height *= pixel_ratio
            last_image = img_li[-1]
            width, height = last_image.size
            box = (0, extra_height, width, height)
            img_li[-1] = last_image.crop(box)

        # Stitch image into one
        # Set up the full screen frame
        img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
        img_frame = Image.new("RGB", (img_li[0].size[0], img_frame_height))
        offset = 0
        for img_frag in img_li:
            img_frame.paste(img_frag, (0, offset))
            offset += img_frag.size[1]
        img_frame.save(save_path)

    def saveScreenshots(self):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]  # fetch the current TestName
        new_name = test_name.split("::")
        filename = new_name[-1] + "_" + self.util.generate_date_time() + ".png"
        screenshotDirectory = "..//logs//screenshots//" + str(datetime.date.today()) + "//"
        relativeFilename = screenshotDirectory + filename

        currentDirectory = os.path.dirname(__file__)
        destinationPath = os.path.join(currentDirectory, relativeFilename)

        destinationFolder = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            #self.driver.save_screenshot(destinationPath)
            self.full_screenshot_with_scroll(self.driver, destinationPath)
            self.cl.info("### Screenshot saved at path: " + destinationPath)
        except Exception as e:
            self.cl.error("### Exception Occurred " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def getInnerText(self, locator, element=None):
        innerText = None
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                innerText = element.get_attribute("innerText")
                self.cl.info("InnerText of element is " + str(innerText))
            else:
                self.cl.error(
                    "Unable to get innerText of element. No element was found for locator :: " + str(
                        locator))
        except Exception as e:
            self.cl.error(
                "Unable to find the value of attribute for element : " + str(
                    locator) + ". Following exception occurred :: " + '. ' + str(
                    e.__class__.__name__) + str(
                    e))
            # print_stack()()
        return innerText

    def isElementDisplayed(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
                if self.enableScreenshot:
                    self.saveScreenshots()

            if element:
                result = element.is_displayed()
                if result:
                    self.cl.info("Element is displayed for locator :: " + str(locator))

                else:
                    self.cl.info("Element is not displayed for locator :: " + str(locator))
            else:
                self.cl.error("Element is not displayed. Unable to find element with locator :: " + str(locator))
                result = False

        except Exception as e:
            self.cl.error(
                "Element is not displayed with locator :: " + str(locator) + " Exception occurred :: " + str(e))
            # print_stack()()
            result = False
        return result

    def scrollingVertical(self, direction):
        direction = direction.lower()
        try:
            if direction == "up":
                self.driver.execute_script("window.scrollBy(0,-1000);")
                self.cl.info("Scrolling the screen up")

            if direction == "down":
                self.driver.execute_script("window.scrollBy(0,700);")
                self.cl.info("Scrolling the screen down")

        except Exception as e:
            self.cl.error("Exception occurred when trying to scroll the screen :: " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def scrollingHorizontal(self, direction):
        direction = direction.lower()
        try:
            if direction == "left":
                self.driver.execute_script("window.scrollBy(-600,0);")
                if self.enableScreenshot:
                    self.saveScreenshots()
                self.cl.info("Scrolling the screen up")

            if direction == "right":
                self.driver.execute_script("window.scrollBy(1100,0);")
                if self.enableScreenshot:
                    self.saveScreenshots()
                self.cl.info("Scrolling the screen down")

        except Exception as e:
            self.cl.error("Exception occurred when trying to scroll the screen :: " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def switchFrame(self, value):
        try:
            self.driver.switch_to.frame(value)
            self.cl.info("Switched to Iframe :: " + str(value))

        except Exception as e:
            self.cl.error("Error while switching to Iframe" + ". Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def switchParentIframe(self):
        try:
            self.driver.switch_to.parent_frame()
            self.cl.info("Switch to Parent iFrame")
        except Exception as e:
            self.cl.error("Unable to switch  to Parent Frame. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def exitIframe(self):
        try:
            self.driver.switch_to.default_content()
            self.cl.info("Switched to default content. Iframe closed")

        except Exception as e:
            self.cl.error("Error while switching to Default Content. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    # def elementSendSpecial(self, locator, message,element=None):
    #     try:
    #         element = self.findElement(locator)
    #         if element:
    #             for items in message:
    #                 element.send_keys(items)
    #         self.cl.info("Text : " + message + " entered on locator: " + str(locator))
    #
    #
    #     except Exception as e:
    #         self.cl.info(
    #             "Unable to send the message on locator: " + str(
    #                 locator["locatorValue"]) + ". Following Exception occurred :: " + str(e))
    #         #print_stack()()

    def slider(self, locator, XCORD, YCORD, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.saveScreenshots()
                self.actions.drag_and_drop_by_offset(source=element, xoffset=XCORD, yoffset=YCORD).perform()
                self.saveScreenshots()
            else:
                self.cl.error(
                    "Unable to perform slider operation on element. No element was found for locator " + str(locator))
        except Exception as e:
            self.cl.error("Exception occurred during sliding. Following Exception occurred :: " + '. ' + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def doubleClick(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.saveScreenshots()
                self.actions.double_click(element).perform()
                self.cl.info("Double Clicked on :: " + str(element))
            else:
                self.cl.error(
                    "Unable to perform double click on element. No element was found for locator :: " + str(locator))
        except Exception as e:
            self.cl.error("Exception occurred during Double Click. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))
            # print_stack()()

    def browserRefresh(self):
        try:
            self.driver.refresh()
            self.cl.info("Refreshing the current window")
        except Exception as e:
            self.cl.error("Unable to refresh the browser. Exception occurred :: " + str(
                e.__class__.__name__) + str(e))

    def currentBrowserWindow(self):
        current_window = None
        try:
            current_window = self.driver.current_window_handle
            self.cl.info("The current window is :: " + str(current_window))

        except Exception as e:
            self.cl.error('Unable to get the current window. Exception Occurred :: ' + str(
                e.__class__.__name__) + str(e))

        return current_window

    def allBrowserWindow(self):
        all_window = None
        try:
            all_window = self.driver.window_handles
            self.cl.info("All available Window's are :: " + str(all_window))

        except Exception as e:
            self.cl.info('Unable to get all the windows. Exception Occurred :: ' + str(
                e.__class__.__name__) + str(e))
        return all_window

    #
    def switchWindow(self, windowNumber: int):
        try:
            allWindow = self.allBrowserWindow()
            self.driver.switch_to.window(allWindow[windowNumber])
            self.cl.info("Switched to new window :: " + str(allWindow[windowNumber]))
        except Exception as e:
            self.cl.info("Unable to switch to new window. Following Exception occurred :: " + str(
                e.__class__.__name__) + " " + str(e))


    def browserBack(self):
        self.driver.back()

    def browserForward(self):
        self.driver.forward()


    def jsClick(self, locator, element=None):
        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.driver.execute_script("arguments[0].click();", element)
            else:
                self.cl.error("Unable to click on element. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to click on element :: " + str(element) + ". Following Exception occurred :: " + str(
                    e.__class__.__name__) + str(e))

    def js_select_list(self, locator, message):
        try:
            element = self.findElement(locator)
            self.driver.execute_script("arguments[0].removeAttribute('readonly','readonly');", element)
            element.send_keys(message)
            self.cl.info("Sending message :: " + str(message) + "locator :: " + str(locator["locatorValue"]))

        except Exception as e:
            self.cl.error("Exception Occurred. Following Exception :: " + str(e))
            # print_stack()()

    def stopPageLoading(self):
        try:
            self.driver.execute_script("return window.stop")
            self.cl.info("Page load stop")
        except Exception as e:
            self.cl.error("Unable to stop the page load. Following Exception occurred :: " + str(
                e.__class__.__name__) + str(e))

    # def js_double_click(self,locator,locatorType):
    #     try:
    #         element = self.findElement(locator,locatorType)
    #         self.driver.execute_script("var evt = document.createEvent('MouseEvents');"+
    #         "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);"+
    #         "arguments[0].dispatchEvent(evt);", element);

    #         self.cl.info("Double clicked element :: " + str(element))

    #     except:
    #         raise Exception
    #         self.cl.info("Unable to Double click element :: " + str(element))

    def rightClick(self, locator, element=None):

        try:
            if locator:
                element = self.findElement(locator)
            if element:
                self.actions.context_click(element).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
                self.saveScreenshots()

            else:
                self.cl.error(
                    "Unable to perform right click on element. No element was found for locator :: " + str(locator))

        except Exception as e:
            self.cl.error(
                "Unable to right click on element " + str(element) + ". Following Exception Occurred :: " + str(
                    e.__class__.__name__) + " " + str(e))

    def getCurrentUrl(self):
        currentUrl = None
        try:
            currentUrl = self.driver.current_url
            print("Current Page URL is :: " + str(currentUrl))

        except Exception as e:
            self.cl.error(
                "Unable to fetch the current URL. Following Exception Occurred :: " + str(
                    e.__class__.__name__) + " " + str(e))

        return currentUrl

    def assertTitle(self, expectedTitle):
        actualTile = self.getTitle()
        assert_that(actualTile).is_equal_to(expectedTitle)

    def assertTitleContains(self, titleSubString):
        result = None
        try:
            result = WebDriverWait(self.driver, 15, 0.2).until(ec.title_contains(titleSubString))
            self.cl.info("The title of page is :: " + str(self.getTitle()))
            self.cl.info("Title of the Page contains text :: " + str(titleSubString))

        except Exception as e:
            self.cl.error("Title of the Page does not contains text :: " + str(
                titleSubString) + ". Following Exception occurred :: " + str(
                e.__class__.__name__) + " " + str(e))
        finally:
            assert_that(result).is_true()

    def assertElementDisplayed(self, locator, element=None):
        assert_that(self.isElementDisplayed(locator, element)).is_true()

    def assertText(self, locator, expectedText, element=None):
        text = self.getElementText(locator, element)
        assert_that(text).is_equal_to(expectedText)

    def assertTextContains(self, textSubString, locator, element=None):
        text = self.getElementText(locator, element)
        assert_that(text).contains_ignoring_case(textSubString)
