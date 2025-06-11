# conftest.py
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from data.locators.home_page_locators import HomePageLocators as home
from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def browser():
    with allure.step('Запуск браузера'):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)

    yield driver
    with allure.step('Закрытие браузера'):
        driver.quit()


@pytest.fixture(scope='function')
def open_main_page(browser):
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        browser.get(Urls.MAIN_PAGE)
        return main_page


@pytest.fixture(scope='function')
def open_auth_page(browser):
    with allure.step("Открытие страницы авторизации"):
        auth_page = LoginPage(browser)
        browser.get(Urls.LOGIN_PAGE)
        return auth_page


@pytest.fixture(scope='function')
def login(open_auth_page):
    with allure.step("Авторизация"):
        page = open_auth_page
        page.fill_field(loc.USERNAME_FIELD, "angular")
        page.fill_field(loc.PASSWORD_FIELD, "password")
        page.fill_field(loc.USERNAME_DESC_FIELD, "angular")
        page.click_element(loc.LOGIN_BUTTON)
        page.wait.until(EC.element_to_be_clickable(home.LOGOUT_BUTTON))
        return page
