"""Contains ManePage class"""
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from ui_tests.pages.base_page import BasePage
from ui_tests.pages.locators import FormLocators
from ui_tests.src.data import FormData, MainPageData


class MainPage(BasePage):
    """Class contains MainPage methods"""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = MainPageData.URL

    def check_popup_is_presented(self, locator: tuple) -> None:
        """Test checks that success message appears"""
        popup = self.driver.find_element(*locator)
        assert popup.is_displayed(), 'Success popup is not presented'
        assert FormData.SUCCESS_TEXT in popup.text, "Success text is not presented"

    def check_popup_is_not_presented(self, locator: tuple) -> None:
        """
        Test checks that
        error message appears and success message doesn't
        when the user sends wrong data into all the fields
        """
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            assert not self.is_element_present(locator), 'It seems that success message appeared'
            assert FormData.UNSUCCESSFUL_TEXT in FormLocators.FORM, 'There is no unsuccessful message in the form'
