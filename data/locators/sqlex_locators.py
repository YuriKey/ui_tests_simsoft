from selenium.webdriver.common.by import By


class SqlexLocators:
    LOGIN_FIELD = (By.XPATH, '//input[@type="text"][@name="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@wfd-id="id1"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@wfd-id="id2"]')
    LOGGED_IN_INDICATOR = (By.XPATH, '//img[@title="Выход..."]')
