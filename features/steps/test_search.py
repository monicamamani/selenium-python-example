from behave import *
# import pytest
from pages.search_page import SearchPage
# from tests.base_test import BaseTest

@given('we have behave installed2')
def step_impl(context):
    pass

@when('we implement a test2')
def step_impl(context):
    # context.page.check_title("DuckDuckGo — Privacy, simplified.")
    assert True is not False

@then('behave will test it for us2!')
def step_impl(context):
    assert context.failed is False

@then('all is ok2')
def step_impl(context):
    assert context.failed is False