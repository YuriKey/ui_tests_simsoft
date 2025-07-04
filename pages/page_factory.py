from pages.alerts_page import AlertsPage
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
