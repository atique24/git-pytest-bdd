import pytest
from selenium import webdriver
from pytest_bdd import given
from pages.mobile_page.mobile_page import MobilePage
from pages.account_creation.account_creation import Account
from utilities.mark_test_status import MarkTestStatus
from pytest_bdd import given,when,then,parsers,scenarios,scenario

driver = None


# ------------------hooks
def pytest_bdd_step_error(request,feature,scenario,step,step_func,step_func_args,exception):
    print(f"step failed ::  {step}")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(request,browser):
    global driver
    if browser == 'Chrome':
        driver = webdriver.Chrome()

    elif browser == 'ff':
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)

    # if request.cls is not None:
    #     request.cls.driver = driver

    yield driver
    driver.quit()

#-------------logic to capture screenshot in the pytest html
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@given("I am in the ecommerce website")
def browser_initialization(setup):
    setup.get("http://live.demoguru99.com/index.php/")


# -----POM Class initialization add below
@pytest.fixture()
def mobile(setup):
    return MobilePage(setup)


@pytest.fixture()
def account(setup):
    return Account(setup)


@pytest.fixture()
def mts(setup):
    return MarkTestStatus(setup)


# --------------common steps add below
@pytest.fixture()
@when("I click on Mobile Tab")
def click_mobile_tab(mobile):
    mobile.mobile_tab()


