from pages.alerts_page import AlertsPage
from pages.app_account_page import AccountPage
from pages.app_customer_login_page import CustomerLoginPage
from pages.app_customers_list_page import CustomersListPage
from pages.app_manager_main_page import ManagerPage
from pages.app_read_user_page import ReadUserPage
from pages.app_registration_page import RegistrationPage
from pages.app_transactions_page import TransactionsPage
from pages.base_page import BasePage
from pages.basic_auth_page import BasicAuthPage
from pages.droppable_page import DndPage
from pages.home_page import HomePage
from pages.lifetime_page import LifetimePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sqlex_page import SqlexPage
from pages.tabs_page import TabsPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self._cache = {}

    @property
    def base(self) -> BasePage:
        if 'base' not in self._cache:
            self._cache['base'] = BasePage(self.driver)
        return self._cache['base']

    @property
    def login(self) -> LoginPage:
        if 'login' not in self._cache:
            self._cache['login'] = LoginPage(self.driver)
        return self._cache['login']

    @property
    def main(self) -> MainPage:
        if 'main' not in self._cache:
            self._cache['main'] = MainPage(self.driver)
        return self._cache['main']

    @property
    def home(self) -> HomePage:
        if 'home' not in self._cache:
            self._cache['home'] = HomePage(self.driver)
        return self._cache['home']

    @property
    def lifetime(self) -> LifetimePage:
        if 'lifetime' not in self._cache:
            self._cache['lifetime'] = LifetimePage(self.driver)
        return self._cache['lifetime']

    @property
    def sqlex(self) -> SqlexPage:
        if 'sqlex' not in self._cache:
            self._cache['sqlex'] = SqlexPage(self.driver)
        return self._cache['sqlex']

    @property
    def dragndrop(self) -> DndPage:
        if 'dragndrop' not in self._cache:
            self._cache['dragndrop'] = DndPage(self.driver)
        return self._cache['dragndrop']

    @property
    def tabs(self) -> TabsPage:
        if 'tabs' not in self._cache:
            self._cache['tabs'] = TabsPage(self.driver)
        return self._cache['tabs']

    @property
    def alerts(self) -> AlertsPage:
        if 'alerts' not in self._cache:
            self._cache['alerts'] = AlertsPage(self.driver)
        return self._cache['alerts']

    @property
    def basic_auth(self) -> BasicAuthPage:
        if 'basic_auth' not in self._cache:
            self._cache['basic_auth'] = BasicAuthPage(self.driver)
        return self._cache['basic_auth']

    @property
    def registration(self) -> RegistrationPage:
        if 'registration' not in self._cache:
            self._cache['registration'] = RegistrationPage(self.driver)
        return self._cache['registration']

    @property
    def manager(self) -> ManagerPage:
        if 'manager' not in self._cache:
            self._cache['manager'] = ManagerPage(self.driver)
        return self._cache['manager']

    @property
    def read_user(self) -> ReadUserPage:
        if 'read_user' not in self._cache:
            self._cache['read_user'] = ReadUserPage(self.driver)
        return self._cache['read_user']

    @property
    def cust_list_page(self) -> CustomersListPage:
        if 'cust_page' not in self._cache:
            self._cache['cust_page'] = CustomersListPage(self.driver)
        return self._cache['cust_page']

    @property
    def customer(self) -> CustomerLoginPage:
        if 'customer' not in self._cache:
            self._cache['customer'] = CustomerLoginPage(self.driver)
        return self._cache['customer']

    @property
    def account(self) -> AccountPage:
        if 'account' not in self._cache:
            self._cache['account'] = AccountPage(self.driver)
        return self._cache['account']

    @property
    def transactions(self) -> TransactionsPage:
        if 'transactions' not in self._cache:
            self._cache['transactions'] = TransactionsPage(self.driver)
        return self._cache['transactions']

    def get_page(self, page_name: str):
        """Для параметризованных тестов."""
        pages = {
            'base': self.base,
            'login': self.login,
            'main': self.main,
            'home': self.home,
            'lifetime': self.lifetime,
            'sqlexec': self.sqlex,
            'dragndrop': self.dragndrop,
            'tabs': self.tabs,
            'alerts': self.alerts,
            'basic_auth': self.basic_auth
        }
        page = pages.get(page_name.lower())
        if not page:
            raise ValueError(f'Unknown page: {page_name}. Available: {list(pages.keys())}')
        return page
