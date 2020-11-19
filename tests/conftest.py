import pytest
from selenium import webdriver
from pytest_bdd import given
from pages.mobile_page.mobile_page import MobilePage
from pages.account_creation.account_creation import Account
from utilities.mark_test_status import MarkTestStatus



#hooks
def pytest_bdd_step_error(request,feature,scenario,step,step_func,step_func_args,exception):
    print(f"step failed ::  {step}")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(request, browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()

    elif browser == 'ff':
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


@given("I am in the ecommerce website")
def browser_initialization(setup):
    setup.get("http://live.demoguru99.com/index.php/")


# -----POM Class initialization
@pytest.fixture()
def mobile(setup):
    return MobilePage(setup)


@pytest.fixture()
def account(setup):
    return Account(setup)


@pytest.fixture()
def mts(setup):
    return MarkTestStatus(setup)
