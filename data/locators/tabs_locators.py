from selenium.webdriver.common.by import By


class TabsLocators:
    LINK_NEW_TAB_LOCATOR = (By.XPATH, '//*[@href="#"][contains(text(), "New Browser Tab")]')
    FRAME_LOCATOR = (By.XPATH, '//iframe[@src="frames-windows/defult1.html"]')