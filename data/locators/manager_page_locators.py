from selenium.webdriver.common.by import By


class ManagerPageLocators:
    MANAGER_LOGIN_BUTTON = (By.XPATH, "//button[@ng-click='manager()']")
    ADD_CUSTOMER_BUTTON = (By.XPATH, "//button[@ng-click='addCust()']")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[@ng-click='openAccount()']")
    CUSTOMERS_LIST_BUTTON = (By.XPATH, "//button[@ng-click='showCust()']")

    FIRST_NAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
    POSTAL_CODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
