"""Contains main page form class"""
import allure
import pytest
from allure import severity, severity_level

from ui_tests.pages.main_page import MainPage
from ui_tests.src.data import FormData


class TestMainPageForm:
    """Contains tests for the main page request form """

    @pytest.mark.skip(reason='Site is alive')
    @allure.title('User sends a correct data into the form')
    @severity(severity_level.CRITICAL)
    @allure.feature('User sends correct data')
    @allure.description('User is scrolling to the bottom and sends correct data')
    @pytest.mark.parametrize('case', FormData.positive_case)
    def test_positive_form_data(self, main_page: MainPage, case: list) -> None:
        """
          Test fills the application with correct data and checks the popup answer
        """
        main_page.fill_the_form(case)
        assert main_page.popup_is_presented(), 'Success popup is not presented'

    @allure.title('User sends an incorrect data into the request form')
    @severity(severity_level.MINOR)
    @allure.feature("User sends an incorrect data")
    @allure.description('User is scrolling to the bottom and sends wrong data')
    @pytest.mark.parametrize('case', FormData.negative_cases)
    def test_negative_form_data(self, main_page: MainPage, case: list) -> None:
        """
          Test fills the application with incorrect data and checks the answer
        """
        main_page.fill_the_form(case)
        assert main_page.error_message_appears(), 'There is no unsuccessful message in the form'
