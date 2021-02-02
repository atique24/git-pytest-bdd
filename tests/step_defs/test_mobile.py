import pytest
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from utilities.mark_test_status import MarkTestStatus

#@pytest.mark.skip
@scenario("..\\features\\ecommerce.feature", "Check Mobile Phone")
def test_one():
    pass

# @when("I click on Mobile Tab")
# def click_mobile_tab(mobile):
#     mobile.mobile_tab()

@pytest.mark.usefixtures("click_mobile_tab")
@then("all available mobiles are displayed")
def mobile_phone_displayed(mobile, mts):
    result = mobile.available_mobiles(expected_list=['Xperia', 'IPhone', 'Samsung Galaxy'])
    mts.finalMark(testcase='Verify all mobiles are available', result=result,
                  resultMessage='Verified all mobiles are available')


extraTypes = {'value': str,
              'value2': list}
convertors = {'name': str,
              'result': str
              }




@scenario("..\\features\\ecommerce.feature",
          scenario_name="Check Sort By functionality",example_converters= convertors)
def test_sort_by_functionality():
    pass


@when('I select Sort By "<Name>"')
@when(parsers.cfparse("I select Sort By {Name:value}",extra_types=extraTypes))
def when_click_sort_by_name(mobile,Name):
    mobile.sort_by(visibleText=Name)


@then(parsers.cfparse("all the available mobiles are sorted by {result:value2}",extra_types=extraTypes))
@then('all the available mobiles are sorted by "<result>"')
def then_mobile_are_sorted(mobile,result,mts):
    result = mobile.verify_sort_functionality(result)
    mts.finalMark(testcase='Sort By',result=result,resultMessage='Sort By Functionality Tested')

