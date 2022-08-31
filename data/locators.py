from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='search_form_input_homepage']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search_button_homepage']")
    RESULTS = (By.XPATH, "//*[@id='links']//*[@data-testid='result']")
    TITLE_ELEMENTS = (By.CSS_SELECTOR, "div.content-info__item__title")
    FIRST_CARD_ELEMENT = (By.CSS_SELECTOR, "div.content-info__item")
    SUBTITLE_CARD_ELEMENT = (By.CSS_SELECTOR, "div.content-info__item__subtitle")
