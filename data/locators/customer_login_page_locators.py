from selenium.webdriver.common.by import By


class CustomerPageLocators:
    CUSTOMER_SELECT = (By.XPATH, '//select[@name="userSelect"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
