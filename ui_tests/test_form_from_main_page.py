import allure
import pytest
from allure import severity, severity_level
from selenium.webdriver.remote.webdriver import WebDriver

from ui_tests.pages.locators import FormLocators
from ui_tests.pages.main_page import MainPage


class TestMainPageForm:

    @pytest.mark.skip(reason='Site is alive')
    @allure.title('User sends a correct data into the form')
    @severity(severity_level.CRITICAL)
    @allure.feature('User sends correct data')
    @allure.description('User is scrolling to the bottom and sends correct data')
    def test_positive_form_data(self, driver: WebDriver, positive_data_case: list) -> None:
        """
          Test fills the application with correct data and checks the popup answer
        """
        page = MainPage(driver)
        page.open()
        for data in positive_data_case:
            page.input_data_to_form(data)
        page.scroll_to_and_click_element(FormLocators.SEND_BUTTON)
        page.expl_wait_for_elem_visibility(FormLocators.POPUP)
        assert check_popup_is_presented(FormLocators.POPUP)

    @allure.title('User sends an incorrect data into the request form')
    @severity(severity_level.MINOR)
    @allure.feature("User sends an incorrect data")
    @allure.description('User is scrolling to the bottom and sends wrong data')
    def test_negative_form_data(self, driver, negative_data_case: list) -> None:
        """
          Test fills the application with incorrect data and checks the answer
        """
        page = MainPage(driver)
        page.open()
        for data in negative_data_case:
            page.input_data_to_form(data)
        page.scroll_to_and_click_element(FormLocators.SEND_BUTTON)
        page.check_popup_is_not_presented(FormLocators.POPUP)
