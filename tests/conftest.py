import logging
import os

import allure
import pytest
from selenium import webdriver
from pytest_bdd import given

from base.SeleniumBase import SeleniumBase
from base.WebDriverFactory import WebDriverFactory
from pages.mobile_page.mobile_page import MobilePage
from pages.account_creation.account_creation import Account
from utilities.customlogger import custom_logger
from utilities.mark_test_status import MarkTestStatus
from pytest_bdd import given,when,then,parsers,scenarios,scenario

driver = None


# ------------------hooks
def pytest_bdd_step_error(request,feature,scenario,step,step_func,step_func_args,exception):
    print(f"step failed ::  {step}")



cl = custom_logger(logging.INFO)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Type in browser type")
    parser.addoption("--screenshot", action="store_true", default=False, help="To enable/disable screenshots")
    parser.addoption("--headless", action="store_true", default=False, help="Browser Headless mode")
    parser.addoption("--url", action="store", default=None, help="URL of the Application under test")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def screenshot(request):
    return request.config.getoption("--screenshot")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")



# ---------------------for new session for each Test class
@pytest.fixture(scope="class")
def oneTimeSetup(request, browser, screenshot, headless):
    wdf = WebDriverFactory(browser, headless)
    SeleniumBase.EnableScreenshotForTest(screenshot)  # ------ Enable / Disable screenshot


    global driver
    driver = wdf.get_browser_instance()

    #if request.cls is not None:
    #request.cls.driver = driver
    yield driver
    driver.quit()
    cl.info("Quiting the browser session")


#-------------logic to capture screenshot in the pytest html
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)


@given("I am in the ecommerce website")
def browser_initialization(oneTimeSetup,url):
    oneTimeSetup.get(url)


# -----POM Class initialization add below
@pytest.fixture()
def mobile(oneTimeSetup):
    return MobilePage(oneTimeSetup)


@pytest.fixture()
def account(oneTimeSetup):
    return Account(oneTimeSetup)



# --------------common steps add below
@pytest.fixture()
@when("I click on Mobile Tab")
def click_mobile_tab(mobile):
    mobile.mobile_tab()


# -------------attach screenshot to allure report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
        allure.attach(
            driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
            )
        sel = SeleniumBase(driver)
        sel.saveScreenshots()


