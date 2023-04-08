"""Contains Cases page class"""

import allure
import pytest
from allure import severity, severity_level

from ui_tests.pages.cases_page import CasesPage
from ui_tests.src.data import CasesData


class TestCasesPage:
    """Contains tests for the cases page"""

    @allure.title('User can see the {case} case')
    @severity(severity_level.NORMAL)
    @allure.feature('User can see all the cases')
    @pytest.mark.parametrize('case, locator', CasesData.cases_list, ids=CasesData.cases_nums_list)
    def test_case_page(self, case: str, locator: tuple, cases_page: CasesPage) -> None:
        """
        test checks availability of each case page(doesn't check content!)
        """
        cases_page.find_and_click_element(locator)
        assert cases_page.should_be_some_page(case), f"This is not a {cases_page.url + case} page"
