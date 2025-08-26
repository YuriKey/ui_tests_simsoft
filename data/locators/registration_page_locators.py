from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    GENDER_FIELD = (By.XPATH, "//select[@id='gender']")
    GENDER_MALE = (By.XPATH, "//option[@value='male']")
    ABOUT_FIELD = (By.XPATH, "//textarea[@id='about']")

    HOBBY_SPORTS = (By.XPATH, "//input[@value='Sports']")
    HOBBY_READING = (By.XPATH, "//input[@value='Reading']")
    HOBBY_TRAVELING = (By.XPATH, "//input[@value='Traveling']")
    ALL_HOBBIES = (By.XPATH, "//div[@class='checkbox-group']")
    HOBBY_LABELS = (By.XPATH, "//div[@class='checkbox-group']//label")

    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(), 'Sample Form')]")
    SAMPLE_FORM_BUTTON = (By.XPATH, "//button[@type='submit']")
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[@ng-click='customer()']")

    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='successMessage']")
