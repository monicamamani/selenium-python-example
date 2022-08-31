# coding=utf-8
import pytest
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = SearchPage(self.driver, self.wait)
        self.page.go_to_search_page()

    @pytest.mark.skip(reason="no way of currently testing this1")
    def test_title(self, load_pages):
        self.page.check_title("DuckDuckGo — Privacy, simplified.")

    @pytest.mark.skip(reason="no way of currently testing this2")
    def test_search(self, load_pages):
        self.page.make_a_search("Selenium")

    @pytest.mark.skip(reason="no way of currently testing this2")
    def test_cards(self, load_pages):
        self.page.check_cards("Selenium")

    def test_2(self, load_pages):
        self.page.default_img()
