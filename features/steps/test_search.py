from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# import pytest
from pages.search_page import SearchPage

@given('we have behave installed2')
def first_step_impl(context):
    context.driver = webdriver.Chrome()
    context.wait = WebDriverWait(context.driver, 10)
    context.searchpage = SearchPage(context.driver, context.wait)
    context.searchpage.go_to_search_page()
    pass

@when('we implement a test2')
def step_impl(context):
    # status = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/img").is_displayed()
    # context.page.check_title("DuckDuckGo — Privacy, simplified.")
    # assert status is True
    # assert True is not False
    status = context.searchpage.default_img()
    assert status is True

@then('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    # context.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(user)
    # print(user)
    # print(pwd, "\n")
    loc_input = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    el = context.searchpage.locate_input_and_enter_value(loc_input, user)
    # context.searchpage.click_enter(el)
    assert context.failed is False

@then('all is ok2')
def step_impl(context):
    context.driver.close()
    # assert context.failed is False