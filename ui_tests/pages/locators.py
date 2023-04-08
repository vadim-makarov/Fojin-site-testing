"""Contains locators for all pages"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Contains locators from the main page"""

    MAIN_PAGE = (By.CSS_SELECTOR, '.sc-fbcb99c0-1 > a:nth-child(1) > img:nth-child(1)')
    ABOUT_US = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(1)')
    SERVICES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(2)')
    STACK = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(3)')
    CASES = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(4)')
    CONTACTS = (By.CSS_SELECTOR, 'a.sc-a0f0d973-0:nth-child(5)')
    VK = (By.CSS_SELECTOR, 'a.sc-5e48d489-4:nth-child(1)')
    TELEGRAM = (By.CSS_SELECTOR, 'a.sc-5e48d489-4:nth-child(2)')
    COOKIES = (By.CSS_SELECTOR, '.sc-2a084499-3')


class CasesLocators:
    """Contains locators for the cases page"""

    CASE_1 = (By.CSS_SELECTOR, "div[href$='cases/1']")
    CASE_2 = (By.CSS_SELECTOR, "div[href$='cases/2']")
    CASE_3 = (By.CSS_SELECTOR, "div[href$='cases/3']")
    CASE_4 = (By.CSS_SELECTOR, "div[href$='cases/4']")
    CASE_5 = (By.CSS_SELECTOR, "div[href$='cases/5']")
    CASE_6 = (By.CSS_SELECTOR, "div[href$='cases/6']")
    CASE_7 = (By.CSS_SELECTOR, "div[href$='cases/7']")
    CASE_8 = (By.CSS_SELECTOR, "div[href$='cases/8']")
    CASE_9 = (By.CSS_SELECTOR, "div[href$='cases/9']")


class FormLocators:
    """Contains locators for the request form"""
    NAME = (By.NAME, 'name')
    EMAIL = (By.NAME, 'email')
    PHONE_NUMBER = (By.NAME, 'phone')
    ABOUT_PROJECT = (By.NAME, 'about')
    SEND_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    POPUP = (By.CSS_SELECTOR, '#form > div > div > div')
    FORM = (By.CSS_SELECTOR, '#form > div > div > form')
