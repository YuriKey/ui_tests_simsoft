from selenium.webdriver.common.by import By


class AlertsLocators:
    FRAME_LOCATOR = (By.XPATH, '//iframe[@src="alert/input-alert.html"]')
    INPUT_ALERT_BUTTON = (By.XPATH, '//*[@href="#example-1-tab-2"]')
    RAISE_ALERT_BUTTON = (By.XPATH, '//button[@onclick="myFunction()"][contains(text(), "demonstrate")]')
    RESULT_MESSAGE = (By.XPATH, '//p[@id="demo"]')
