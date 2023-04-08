"""Contains Cases Page Class"""
from selenium.webdriver.remote.webdriver import WebDriver

from ui_tests.pages.main_page import MainPage
from ui_tests.src.data import CasesData


class CasesPage(MainPage):
    """Contains Cases page methods"""
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = CasesData.URL
