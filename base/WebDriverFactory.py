from selenium import webdriver

class WebDriverFactory():
    def __init__(self,browser):
        self.browser = browser

    def get_browser_instance(self):
        if self.browser == "FF":
            driver = webdriver.Firefox()

        elif self.browser == "Chrome":
            driver = webdriver.Chrome()

        elif self.browser == "IE":
            driver = webdriver.Ie()

        else:
            driver = webdriver.Chrome()


        baseUrl = "http://live.demoguru99.com/index.php/"
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseUrl)

        return driver



