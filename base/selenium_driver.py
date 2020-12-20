from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from utilities.customlogger import custom_logger
import logging
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
from selenium.webdriver.support.color import Color


class SeleniumDriver():
    cl = custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

        self.actions = ActionChains(self.driver)

    def ByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial link":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "class":
            return By.CLASS_NAME

        else:
            self.cl.info("Invalid Locatortype " + str(locatorType))

    def findElement(self, locator, locatorType):
        element = None
        try:
            bytype = self.ByType(locatorType)
            element = self.driver.find_element(bytype, locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element);
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element);
            self.cl.info(
                "Element found with locatorType : " + str(locatorType) + " & locator : " + str(locator) + str(element))

        except Exception as e:
            self.cl.info(
                "Element could not be found with type : " + str(locatorType) + " and locator : " + str(locator) + str(
                    e))
            print_stack()

        return element

    def findElements(self, locator, locatorType):
        element = []
        try:
            bytype = self.ByType(locatorType)
            element = self.driver.find_elements(bytype, locator)
            self.cl.info("Element found with locatorType : " + str(locatorType) + "& locator : " + str(locator))

        except Exception as e:
            self.cl.info(
                "Element could not be found with locatortype : " + str(locatorType) + " and locator : " + str(
                    locator) + "exception:: " + str(e))
            print_stack()
        return element

    def get_element_dropdown_value(self, locator, locatorType, selectType, value):
        try:
            element = self.findElement(locator, locatorType)

            sel = Select(element)
            if selectType == "Value":
                sel.select_by_value(value)
                self.cl.info("Selected element with Name " + str(value) + " from the drop down using Value")

            elif selectType == "text":
                sel.select_by_visible_text(value)
                self.cl.info("Selected element with value " + str(value) + " from the drop down using Visible Text")

            elif selectType == "index":
                sel.select_by_index(value)
                self.cl.info("Selected element with index " + str(value) + " from the drop down using Index position")

        except Exception as e:
            self.cl.info("Unable to select element from the dropdown. Exception occurred :: " + str(e))
            print_stack()

    def elementClick(self, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            element.click()
            self.cl.info("Clicked on Element : " + str(element))

        except Exception as e:
            self.cl.info("Unable to click the element: " + locator + ". Exception occured :: " + str(e))
            print_stack()

    def elementSend(self, locator, locatorType, message):
        try:
            element = self.findElement(locator, locatorType)
            element.clear()
            element.send_keys(message)
            self.cl.info("Text : " + str(message) + " entered on locator: " + locator)
        except Exception as e:
            self.cl.info("Unable to send the message on locator: " + locator + "Exception :: " + str(e))
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getText(self, locator, locatorType):
        element_text = None
        try:
            element = self.findElement(locator, locatorType)
            element_text = element.text
            self.cl.info("Text of the element : " + locator + " is " + element_text)
            return element_text
        except Exception as e:
            self.cl.info(
                "Unable to find the text for element : " + locator + ". Following Exception occured :: " + str(e))
            print_stack()
        return element_text

    def getTextElementList(self, locator, locatorType):
        elementText = []
        elementText2 = []
        try:
            element = self.findElements(locator, locatorType)
            for item in element:
                itemtext = item.text
                elementText.append(itemtext)

            elementText2 = list(filter(None, elementText))
            self.cl.info(elementText2)
            return elementText2

        except Exception as e:
            self.cl.info("Unable to return text for elements. Following Exception occured :: " + str(e))
            print_stack()
        return elementText2

    def getAttribute(self, locator, locatorType, attributeType):
        elementAttribute = None
        try:
            element = self.findElement(locator, locatorType)
            elementAttribute = element.get_attribute(attributeType)
            self.cl.info("Value of Attribute :: " + attributeType + " is " + str(elementAttribute))
            return elementAttribute
        except Exception as e:
            self.cl.info(
                "Unable to find the value of attribute for element : " + locator + ". Following exception occured :: " + str(
                    e))
            print_stack()
        return elementAttribute

    def getAttributelist(self, locator, locatorType, attributeType):
        element_attribute = []

        try:
            element = self.findElements(locator, locatorType)
            for item in element:
                elementAttribute = item.get_attribute(attributeType)
                element_attribute.append(elementAttribute)
                self.cl.info("Value of Attribute :: " + attributeType + " is " + elementAttribute)
            return element_attribute

        except Exception as e:
            self.cl.info("Unable to find the value of attribute for element : " + locator + " exception :: " + str(e))
            print_stack()
        return element_attribute

    def get_value_of_css_property(self, locator, locatorType, attributeType):
        try:
            element = self.findElement(locator, locatorType)
            cssAttributeProperty = element.value_of_css_property(property_name=attributeType)
            self.cl.info("Value of CSS Attribute :: " + attributeType + " is " + cssAttributeProperty)
            if attributeType == 'Color':
                formatted_name = Color.from_string(cssAttributeProperty).hex
                self.cl.info("Value of CSS Attribute :: " + attributeType + " in HEX format is " + cssAttributeProperty)
                return formatted_name
            else:
                return cssAttributeProperty
        except Exception as e:
            self.cl.info(
                "Unable to find the value of attribute for element : " + locator + ". Following Exception Occured :: " + str(
                    e))
            print_stack()
        return cssAttributeProperty

    def explicitwait(self, locator, locatorType, time, poll):
        try:
            bytype = self.ByType(locatorType)
            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[ElementNotInteractableException, ElementNotVisibleException,
                                                     NoSuchElementException, TimeoutException,
                                                     StaleElementReferenceException, ElementClickInterceptedException])
            self.cl.info("Waiting to click on element : " + locator + "for time " + str(time) + "sec")
            element = wait.until(EC.element_to_be_clickable((bytype, locator)))
            self.cl.info("Element is Available for action")

        except:
            self.cl.info("Unable to find the element")
            print_stack()

    def explicit_wait_for_iframe(self, locator, index, time, poll):
        try:

            wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll,
                                 ignored_exceptions=[NoSuchFrameException, NoSuchElementException, TimeoutException])
            self.cl.info("Waiting to find : " + locator + "with index position:: " + str(index) + "for time " + str(
                time) + "sec")
            element = wait.until(
                EC.frame_to_be_available_and_switch_to_it((self.driver.find_elements_by_tag_name(locator)[index])))
            self.cl.info("iFrame is Available for switching")

        except TimeoutException:
            self.cl.info("Unable to find the element")

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.findElements(locator, locatorType)
            self.cl.info(element)
            if len(element) > 0:
                self.cl.info("Element with locator " + str(locator) + "is present")
                return True
            else:
                self.cl.info("Element with locator " + str(locator) + "is not present")
                return False

        except Exception as e:
            self.cl.info("exception occured :: " + str(e))
            return False
            print_stack()

    def elementclear(self, locator, locatorType):
        element = None
        try:
            element = self.findElement(locator, locatorType)
            element.clear()
            self.cl.info("Cleared Element : " + str(element))

        except:
            raise Exception
            self.cl.info("Unable to find element")
            print_stack()

    def savescreenshots(self, resultMessage):
        filename = resultMessage + str(round(time.time() * 10000)) + ".png"
        screenshotDirectory = "..//screenshots//"
        relativeFilename = screenshotDirectory + filename

        currentDirectory = os.path.dirname(__file__)
        destinationPath = os.path.join(currentDirectory, relativeFilename)

        destinationFolder = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)
            self.driver.save_screenshot(destinationPath)
            self.cl.info("### Screenshot saved at path: " + destinationPath)
        except:
            self.cl.warning("### Exception Occured")
            print_stack()

    def isElementDisplayed(self, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            isDisplayed = element.is_displayed()

            if isDisplayed is True:
                self.cl.info("Element is displayed with locator :: " + str(locator))
                return True
            else:
                self.cl.info("Element is not displayed with locator :: " + str(locator))
                return False

        except Exception as e:
            self.cl.warning("Exception occured while executing isElementDisplayed :: exception occured :: " + str(e))
            return False
            print_stack()

    def scrollingVertical(self, direction):
        direction = direction.lower()
        try:
            if direction == "up":
                self.driver.execute_script("window.scrollBy(0,-1000);")
                self.cl.info("Scrolling the screen up")

            if direction == "down":
                self.driver.execute_script("window.scrollBy(0,700);")
                self.cl.info("Scrolling the screen down")

        except:
            self.cl.warning("Exception occured when trying to scroll the screen")
            print_stack()

    def scrollingHorizontal(self, direction):
        direction = direction.lower()
        try:
            if direction == "left":
                self.driver.execute_script("window.scrollBy(-600,0);")
                self.cl.info("Scrolling the screen up")

            if direction == "right":
                self.driver.execute_script("window.scrollBy(1100,0);")
                self.cl.info("Scrolling the screen down")

        except:
            self.cl.warning("Exception occured when trying to scroll the screen")
            print_stack()

    def switchFrame(self, value):
        try:
            self.driver.switch_to.frame(value)
            self.cl.info("Switched to Iframe :: " + str(value))

        except Exception as e:
            self.cl.error("Error while switching to Iframe" + ". Following Exception occured :: " + str(e))
            print_stack()

    def switchParentFrame(self):
        try:
            self.driver.switch_to.parent_frame()
        except Exception as e:
            self.cl.info("Unable to  to Parent Frame. Following Exception occured :: " + str(e))
            print_stack()

    def switch_default_content(self):
        try:
            self.driver.switch_to.default_content()
            self.cl.info("Switched to default content")

        except Exception as e:
            self.cl.error("Error while switching to Default Content. Exception occurred :: " + str(e))
            print_stack()

    def elementSendSpecial(self, locator, locatorType, message):
        try:
            element = self.findElement(locator, locatorType)
            for items in message:
                element.send_keys(items)
            self.cl.info("Text : " + message + " entered on locator: " + locator)
        except Exception as e:
            self.cl.info(
                "Unable to send the message on locator: " + locator + ". Following Exception occured :: " + str(e))
            print_stack()

    def slider(self, locator, locatorType, xcord, ycord):
        try:
            element = self.findElement(locator, locatorType)
            self.actions.drag_and_drop_by_offset(source=element, xoffset=xcord, yoffset=ycord).perform()
        except Exception as e:
            self.cl.info("Exception orrcured during sliding. Following Exception occured :: " + str(e))
            print_stack()

    def double_clickk(self, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            self.actions.double_click(element).perform()
            self.cl.info("Double Clicked on :: " + str(element))
        except Exception as e:
            self.cl.info("Exception occurred during Double Click. Following Exception occurred :: " + str(e))
            print_stack()

    def browserRefresh(self):
        self.driver.refresh()

    def current_handle_window(self):
        current_window = self.driver.current_window_handle
        self.cl.info("The current window handle is :: " + str(current_window))
        return current_window

    def all_window_handles(self):
        all_handles = self.driver.window_handles
        self.cl.info("All available Window's are :: " + str(all_handles))
        return all_handles

    def switching_to_window(self):
        try:
            current_window = self.current_handle_window()
            all_windows = self.all_window_handles()

            for items in all_windows:
                if items != current_window:
                    self.driver.switch_to.window(items)
                    self.cl.info("Switched to window :: " + str(items))

        except Exception as e:
            self.cl.info("Unable to switch to new window. Following Exception occurred :: " + str(e))

    def switch_to_parent_window(self):
        try:
            all_windows = self.all_window_handles()

            for items in all_windows:
                if items == all_windows[0]:
                    self.driver.switch_to.window(items)
                    self.cl.info("Switched to window :: " + str(items))

        except Exception as e:
            self.cl.info("Unable to  to new window. Following Exception occurred :: " + str(e))

    def browserback(self):
        self.driver.back()

    def browserForward(self):
        self.driver.forward()

    def action(self):
        try:
            self.actions.key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
            # self.actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        except Exception as e:
            self.cl.info("Unable to press ENTER key. Following Exception occurred :: " + str(e))


    def enter(self):
        try:
            self.actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            self.cl.info("Pressed ENTER")
        except Exception as e:
            self.cl.info("Unable to press ENTER key. Following Exception occurred :: " + str(e))

    def close_new_window(self):
        try:
            self.actions.key_down(Keys.CONTROL).send_keys('W').perform()
            self.cl.info("Pressing CTRL + W to close the new window")
        except Exception as e:
            self.cl.info("Unable to perform Action :: CTRL + W. Following Exception occurred :: " + str(e))
            print_stack()

    def js_element_click(self, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            self.driver.execute_script("arguments[0].click();", element);

        except Exception as e:
            self.cl.info(
                "Unable to click on element :: " + str(element) + ". Following Exception occurred :: " + str(e))

    def js_select_list(self, locator, locatorType, message):
        try:
            element = self.findElement(locator, locatorType)
            self.driver.execute_script("arguments[0].removeAttribute('readonly','readonly');", element)
            element.send_keys(message)
            self.cl.info("Sending message :: " + str(message) + "locator :: " + str(locator))

        except Exception as e:
            self.cl.info("Exception Occured. Following Exception :: " + str(e))
            print_stack()

    def stop_page_load(self):
        try:
            self.driver.execute_script("return window.stop");
            self.cl.info("Page load stop")
        except Exception as e:
            self.cl.info("Unable to stop the page load. Following Exception occurred :: " + str(e))

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

    def right_clickk(self, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            self.actions.context_click(element).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

        except Exception as e:
            self.cl.info(
                "Unable to right click on element " + str(element) + ". Following Exception Occured :: " + str(e))
