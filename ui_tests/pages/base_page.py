"""Module contains Base Page class"""
from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.locators import MainPageLocators


class BasePage:
    """Class contains common methods"""

    def __init__(self, driver: WebDriver, timeout=20) -> None:
        self.driver = driver
        self.url = None
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency=1)

    def open(self) -> None:
        """Opens passed url"""
        self.driver.get(self.url)

    def is_element_present(self, locator: tuple):
        """Checks if element presented on the page"""
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return True

    def is_element_active(self, locator: tuple):
        """Checks if element active"""
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
        except ElementClickInterceptedException:
            return False
        return True

    def find_and_click_element(self, locator: tuple):
        """Waits for an item to appear, moves to it and clicks it"""
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()
        return self

    def should_be_some_page(self, page_name: str) -> bool:
        """Checks that the name of the current page contains the passed url"""
        try:
            self.wait.until(EC.url_contains(page_name))
        except TimeoutException:
            return False
        return True

    def go_to_the_next_window(self):
        """Waits for a new window to open and switches to it"""
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        return self

    def find_element_and_input_data(self, locator: tuple, data: str):
        """Waits for the field to appear on the page, clears it and enters the text"""
        self.wait.until(EC.element_to_be_clickable(locator))
        field = self.driver.find_element(*locator)
        field.send_keys(data)
        return self

    def accept_cookie(self):
        """Нажимает кнопку ок на попапе куки еслм баннер появился"""
        if self.is_element_present(MainPageLocators.COOKIES):
            self.find_and_click_element(MainPageLocators.COOKIES)
        return self
