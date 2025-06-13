import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from data.locators.home_page_locators import HomePageLocators as hloc
from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls
from pages.page_factory import PageFactory


@pytest.fixture
def pages(browser):
    with allure.step('Инициализация страницы'):
        return PageFactory(browser)


@pytest.fixture(scope='function')
def browser():
    with allure.step('Запуск браузера'):
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)

    yield driver
    with allure.step('Закрытие браузера'):
        driver.quit()


@pytest.fixture(scope='function')
def open_main_page(pages):
    with allure.step('Открытие главной страницы'):
        pages.main.open(Urls.MAIN_PAGE)
        return pages.main


@pytest.fixture(scope='function')
def open_auth_page(pages):
    with allure.step('Открытие страницы авторизации'):
        pages.login.open(Urls.LOGIN_PAGE)
        return pages.login


@pytest.fixture(scope='function')
def login(open_auth_page, pages):
    with allure.step('Авторизация'):
        page = open_auth_page
        page.fill_field(loc.USERNAME_FIELD, 'angular')
        page.fill_field(loc.PASSWORD_FIELD, 'password')
        page.fill_field(loc.USERNAME_DESC_FIELD, 'angular')
        page.click_element(loc.LOGIN_BUTTON)

        open_auth_page.is_element_visible(hloc.LOGOUT_BUTTON), 'Кнопка выхода не отобразилась после логина'
        return pages.home
