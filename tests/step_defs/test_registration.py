from pytest_bdd import given,when,then,scenario,scenarios,parsers


extraTypes = {'value': str}
exampleConvertors = {'firstname': str,
              'lastname': str,
              'email': str,
              'password': str,
              'confirm': str,
              'name' : str,
              'result' : list
              }


@scenario("C:\\Users\\A610037\\PycharmProjects\\pytest-bdd\\tests\\features\\registration.feature",'Registration',
          example_converters=exampleConvertors)

def test_registration():
    pass


@when("I click on Account")
@when("I select Register option from dropdown menu")
def click_account(account):
    account.click_account()


@when(parsers.cfparse(
    'I enter "{firstname:value}" "{lastname:value}" "{email:value}" "{password:value}""{confirm:value}"',
    extra_types=extraTypes))
@when('I enter "<firstname>" "<lastname>" "<email>" "<password>" "<confirm>"')
def provide_registration_data(account,firstname, lastname, email, password, confirm):
    account.fill_registration(firstname, lastname, email, password, confirm)


@when("I select the checkbox")
def select_checkbox(account):
    account.checkbox()


@when("I click the Register button")
def click_register_button(account):
    account.click_registration_button()


@then(parsers.cfparse('I see the "{success:value}" message', extra_types=extraTypes))
@then('I see the "<success>" message')
def successful_registration(account, mts, success):
    result = account.success_message(success)
    mts.finalMark(testcase='Account Registration', result=result,
                  resultMessage='Registration successful')