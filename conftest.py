"""basic file contains common fixtures"""

from typing import Generator

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.cases_page import CasesPage
from ui_tests.pages.main_page import MainPage


@pytest.fixture
def driver(request) -> Generator:
    """
    the fixture downloads the latest driver and creates the browser instance with passed options
    """
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1920, 1080)
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        screenshot(browser, test_name)
    browser.quit()


def screenshot(browser, name: str) -> None:
    """Gets a screenshot and attaches it to the report"""
    allure.attach(browser.get_screenshot_as_png(), name=f"Screenshot fail_{name}",
                  attachment_type=AttachmentType.PNG)


@pytest.fixture
def main_page(driver) -> MainPage:
    """Opens a main page"""
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def cases_page(driver) -> MainPage:
    """Opens a main page"""
    page = CasesPage(driver)
    page.open()
    return page
