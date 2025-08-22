import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from data.locators.home_page_locators import HomePageLocators as hloc
from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls
from drivers.driver_factory import DriverFactory
from pages.page_factory import PageFactory
from utils.cookies_helper import CookiesHelper as ch

urls = Urls()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests (chrome, firefox, edge)")
    parser.addoption("--grid", action="store_true", default=False,
                     help="Use Selenium Grid")
    parser.addoption("--grid-url", action="store", default="http://localhost:4444/wd/hub",
                     help="Selenium Grid URL")


@pytest.fixture
def browser(request):
    with allure.step('Инициализация драйвера'):
        browser_name = request.config.getoption("--browser")
        use_grid = request.config.getoption("--grid")
        grid_url = request.config.getoption("--grid-url")

        driver = DriverFactory.create_driver(
            browser_name=browser_name,
            use_grid=use_grid,
            grid_url=grid_url
        )

        yield driver

        driver.quit()


@pytest.fixture
def pages(browser):
    with allure.step('Инициализация страницы'):
        return PageFactory(browser)


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


@pytest.fixture
def create_user(pages):
    with allure.step('Создание пользователя со случайными данными'):
        man_page = pages.manager
        man_page.open(urls.APP_LOGIN_PAGE)
        user_data = man_page.create_random_customer()
        return user_data


@pytest.fixture
def create_active_account(pages):
    with allure.step('Создание активного счета'):
        man_page = pages.manager
        read_page = pages.read_user
        man_page.open(urls.APP_LOGIN_PAGE)
        user_data = man_page.create_random_customer()
        man_page.open_account_button()
        read_page.fill_customer_name(f"{user_data['first_name']} {user_data['last_name']}")
        read_page.fill_currency()
        read_page.click_process_button()
        man_page.switch_to_alert()
        man_page.accept_alert()
        read_page.click_home_button()
        return user_data


@pytest.fixture
def login_new_user(pages, create_active_account):
    with allure.step('Авторизация пользователя с активным счетом'):
        reg_page = pages.registration
        cust_page = pages.customer
        user_data = create_active_account
        user_full_name = f"{user_data['first_name']} {user_data['last_name']}"
        reg_page.click_customer_login()
        cust_page.customer_select(user_full_name)
        cust_page.click_login_button()


@pytest.fixture
def login_new_user_with_notnull_balance(pages, login_new_user):
    acc_page = pages.account
    acc_page.click_deposit_button()
    acc_page.fill_amount_field(amount=100321)
    acc_page.click_submit_button()


@pytest.fixture
def login_new_user_with_history(pages, login_new_user_with_notnull_balance):
    acc_page = pages.account
    deposit_values = (
        acc_page.get_random_deposit_amount(current_balance=10000),
        acc_page.get_random_deposit_amount(current_balance=10000),
        acc_page.get_random_deposit_amount(current_balance=10000)
        )
    withdraw_values = (
        acc_page.get_random_deposit_amount(current_balance=10000),
        acc_page.get_random_deposit_amount(current_balance=10000),
        acc_page.get_random_deposit_amount(current_balance=10000)
    )
    for value in deposit_values:
        acc_page.fill_amount_field(value)
        acc_page.click_submit_button()

    acc_page.click_withdrawl_button()

    for value in withdraw_values:
        acc_page.fill_amount_field(value)
        acc_page.click_submit_button()
