"""Contains ManePage class"""
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from ui_tests.pages.base_page import BasePage
from ui_tests.pages.locators import FormLocators
from ui_tests.src.data import FormData, MainPageData


@pytest.mark.cases
class MainPage(BasePage):
    """Class contains MainPage methods"""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = MainPageData.URL

    def fill_the_form(self, case: list):
        """Fills the request form and sends it"""
        self.find_element_and_input_data(FormLocators.NAME, case[0]) \
            .find_element_and_input_data(FormLocators.EMAIL, case[1]) \
            .find_element_and_input_data(FormLocators.PHONE_NUMBER, case[2]) \
            .find_element_and_input_data(FormLocators.ABOUT_PROJECT, case[3]) \
            .find_and_click_element(FormLocators.SEND_BUTTON)
        return self

    def popup_is_presented(self) -> bool:
        """Checks that success message appears"""
        return self.is_element_present(FormLocators.POPUP)

    def error_message_appears(self) -> bool:
        """
        Checks that error message appears
        when the user sends wrong data into all the fields
        """
        form_text = self.driver.find_element(*FormLocators.FORM).text
        return FormData.unsuccessful_text in form_text
