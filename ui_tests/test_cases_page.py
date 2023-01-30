import os

import allure
import pytest
from allure import severity, severity_level

from ui_tests.pages.cases_page import CasesPage
from ui_tests.pages.data import CasesData

# username = os.environ.get('USERNAME') or 'username'
# password = os.environ.get('PASSWORD') or 'password'


class TestCasesPage:
    URL = f'https://fojin.tech/ru/cases/'

    @allure.title('User can see the {case} case')
    @severity(severity_level.NORMAL)
    @allure.feature('User can see all the cases')
    @pytest.mark.parametrize('case, locator', list(zip(CasesData.CASES_LIST, CasesData.LOCATORS)))
    def test_case_page(self, browser, case: str, locator: tuple) -> None:
        """
        test checks availability of each case page(doesn't check content!)
        """
        page = CasesPage(browser, self.URL)
        page.open()
        page.expl_wait_for_page_download('cases')
        page.scroll_to_and_click_element(locator)
        page.expl_wait_for_page_download(case)
        page.should_be_some_page(case)
