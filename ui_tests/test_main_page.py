"""Module contains tests for main page"""
import allure
import pytest
from allure import severity, severity_level

from ui_tests.pages.main_page import MainPage
from ui_tests.src.data import MainPageData


class TestMainPage:
    """Class contains  tests for main page and related links"""

    @severity(severity_level.CRITICAL)
    @allure.feature('User can go to all top links')
    @allure.title('User can see and go to the "{endpoint}" link')
    @pytest.mark.parametrize('endpoint, locator', list(zip(MainPageData.ENDPOINTS, MainPageData.LINKS_LIST)))
    def test_link_names(self, main_page: MainPage, endpoint: str, locator: tuple) -> None:
        """user can go to all top links from the main page"""
        main_page.find_and_click_element(locator)
        assert main_page.should_be_some_page(endpoint), f"This in not a {endpoint} page"

    @severity(severity_level.MINOR)
    @allure.feature('User can go to the policy page and to the social page links')
    @allure.title('User can see and go to the "{element}" link')
    @pytest.mark.parametrize('endpoint, locator',
                             list(zip(MainPageData.BOTTOM_ENDPOINTS, MainPageData.BOTTOM_ELEM_LIST)))
    def test_bottom_elements_are_active(self, endpoint: str, locator: tuple, main_page: MainPage) -> None:
        """
        user can go to all bottom links from the main page
        """
        main_page.accept_cookie() \
            .find_and_click_element(locator) \
            .go_to_the_next_window()
        assert main_page.should_be_some_page(endpoint), f"This in not a {endpoint} page"
