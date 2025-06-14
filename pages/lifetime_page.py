from pages.base_page import BasePage


class LifetimePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'lifetime_url_title': 'Lifetime Membership Club | Free Selenium, Webservices Tutorials'
    }
