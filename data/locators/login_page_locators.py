from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    USERNAME_DESC_FIELD = (By.XPATH, '//input[@name="formly_1_input_username_0"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@class="btn btn-danger"]')
    ALERT_LOGIN_ERROR = (By.XPATH, '//*[@class="alert alert-danger ng-binding ng-scope"]')
