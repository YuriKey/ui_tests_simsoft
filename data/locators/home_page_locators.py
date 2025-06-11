from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='#/login']")
    SUCCESS_MESSAGE = (By.XPATH, '//p[@class="ng-scope"][contains(text(), "You\'re logged in!!")]')
