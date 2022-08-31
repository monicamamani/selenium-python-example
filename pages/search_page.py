from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import SearchPageLocators
from selenium.webdriver.common.keys import Keys
import array as arr


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://google.com"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        assert self.get_title() == title

    def make_a_search(self, input_text):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))
        self.driver.save_screenshot("results/results.png")

    def check_cards(self, arr_elements):
        # Evaluating entire DOM
        elements = self.driver.find_elements(*self.locator.TITLE_ELEMENTS)
        print(len(elements))
        for e in elements:
            print(e.text)

        # self.driver.quit()

        #Evaluating a subset of the DOM
        els = self.driver.find_element(*self.locator.FIRST_CARD_ELEMENT)
        subtitle = els.find_element(*self.locator.SUBTITLE_CARD_ELEMENT)
        print(subtitle.text)

    def default_img(self):
        # Get attribute of current active element
        status = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/img").is_displayed()
        return status

    def locate_input_and_enter_value(self, xpath_exp, value):
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(user)
        element = self.driver.find_element_by_xpath(xpath_exp)
        element.send_keys(value)
        element.submit()

    def click_enter(self, element):
        element.submit()




