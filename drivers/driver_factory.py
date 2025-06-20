from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    @staticmethod
    def _create_local_driver(browser_name):
        if browser_name == "chrome":
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=webdriver.ChromeOptions()
            )
        elif browser_name == "firefox":
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=webdriver.FirefoxOptions()
            )
        elif browser_name == "edge":
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=webdriver.EdgeOptions()
            )
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.maximize_window()
        return driver

    @staticmethod
    def _create_remote_driver(browser_name, grid_url):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser for Grid: {browser_name}")

        options.set_capability("browserName",
                               "chrome" if browser_name == "chrome" else
                               "firefox" if browser_name == "firefox" else
                               "MicrosoftEdge")
        options.set_capability("platformName", "windows")

        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )

        driver.maximize_window()
        return driver

    @staticmethod
    def create_driver(browser_name, use_grid=False, grid_url="http://localhost:4444/wd/hub"):
        browser_name = browser_name

        if use_grid:
            return DriverFactory._create_remote_driver(browser_name, grid_url)
        else:
            return DriverFactory._create_local_driver(browser_name)
