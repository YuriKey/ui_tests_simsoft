from selenium.webdriver.common.by import By


class CustomersListLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@ng-model='searchCustomer']")
    DELETE_BUTTON = (By.XPATH, "//button[@ng-click='deleteCust(cust)']")
