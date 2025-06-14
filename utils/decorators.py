from functools import wraps

import allure
from selenium.webdriver.remote.webdriver import WebDriver


def screenshot_on_failure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            driver = None

            for item in list(args) + list(kwargs.values()):
                if hasattr(item, 'browser'):
                    driver = item.browser
                    break

                if hasattr(item, 'driver'):
                    driver = item.driver
                    break

            if driver and isinstance(driver, WebDriver):
                try:
                    allure.attach(
                        driver.get_screenshot_as_png(),
                        name=f"screenshot_{func.__name__}",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as screenshot_error:
                    print(f"Failed to take screenshot: {screenshot_error}")

            raise e

    return wrapper
