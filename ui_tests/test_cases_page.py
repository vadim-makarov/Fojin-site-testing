import allure
import pytest
from allure import severity, severity_level

from ui_tests.pages.cases_page import CasesPage
from ui_tests.src.data import CasesData


class TestCasesPage:

    @allure.title('User can see the {case} case')
    @severity(severity_level.NORMAL)
    @allure.feature('User can see all the cases')
    @pytest.mark.parametrize('case, locator', list(zip(CasesData.CASES_LIST, CasesData.LOCATORS)))
    def test_case_page(self, driver, case: str, locator: tuple) -> None:
        """
        test checks availability of each case page(doesn't check content!)
        """
        page = CasesPage(driver, self.URL)
        page.open()
        page.expl_wait_for_page_download('cases')
        page.scroll_to_and_click_element(locator)
        page.expl_wait_for_page_download(case)
        page.should_be_some_page(case)
