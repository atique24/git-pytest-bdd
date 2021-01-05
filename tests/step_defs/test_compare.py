from pytest_bdd import given, when, then, scenarios, scenario, parsers
import pytest

example_convertors = {
    "mobile1": str,
    "mobile2": str
}

extra_types = {
    "value": str
}


@scenario("C:\\Users\\A610037\\PycharmProjects\\git-pytest-bdd\\tests\\features\\compare.feature", "Compare Mobile",
          example_converters=example_convertors)
def test_compare_functionality():
    pass


# @when("I click on Mobile Tab")
# def click_mobile_tab(mobile):
#     mobile.mobile_tab()


@pytest.mark.usefixtures("click_mobile_tab")    # use the common fixture from conftest
@when(parsers.cfparse("I click on Add to Compare for '{mobile1:value}'", extra_types=extra_types))
@when("I click on Add to Compare for '<mobile1>'")
def when_step1(mobile, mobile1):
    mobile.add_product1_for_compare(mobile1)


@when(parsers.cfparse("I click on Add to Compare for '{mobile2:value}'", extra_types=extra_types))
@when("I click on Add to Compare for '<mobile2>'")
def when_step2(mobile, mobile2):
    mobile.add_product2_for_compare(mobile2)


@when("I click compare button")
def when_step3(mobile):
    mobile.click_compare_button()


@then("compare products page is displayed.")
def then_step1(mobile, mts):
    result = mobile.confirm_compare_window()
    mts.finalMark(testcase="compare functionality", result=result, resultMessage="Product compare successfully")

