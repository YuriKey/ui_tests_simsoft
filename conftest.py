import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from data.locators.home_page_locators import HomePageLocators as hloc
from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls
from pages.page_factory import PageFactory
from utils.cookies_helper import CookiesHelper as ch


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


@pytest.fixture
def setup(browser):
    browser.delete_all_cookies()
    yield


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = None

        for fixture_name in item.fixturenames:
            fixture = item.funcargs.get(fixture_name)

            if hasattr(fixture, 'driver'):
                driver = fixture.driver
                break
            elif hasattr(fixture, 'browser'):
                driver = fixture.browser
                break
            elif isinstance(fixture, WebDriver):
                driver = fixture
                break

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"screenshot_{item.nodeid.replace('::', '_')}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                raise Exception(f'Не удалось выполнить скриншот: {str(e)}')


@pytest.fixture
def prepare_auth_cookies(pages, request, tmp_path):
    with allure.step('Авторизация через cookies'):
        cookies_file = tmp_path / "test_cookies.json"
        sqlex_page = pages.sqlex.open_page()
        cookies_helper = ch(sqlex_page, str(cookies_file))

        sqlex_page.sqlex_login()

        cookies = cookies_helper.get_cookies()

        ch.save_cookies_to_file(cookies, str(cookies_file))

        cookies_helper.delete_browser_cookies()

        request.addfinalizer(cookies_helper.cleanup)

        return cookies_file
