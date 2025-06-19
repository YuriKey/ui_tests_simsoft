from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.ie.options import Options as IeOptions


class DriverFactory:
    @staticmethod
    def _create_local_driver(browser_name):
        common_args = ['--start-maximized']

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            for arg in common_args:
                options.add_argument(arg)
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            for arg in common_args:
                options.add_argument(arg)
            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            for arg in common_args:
                options.add_argument(arg)
            return webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )

        elif browser_name == "ie":
            options = IeOptions()
            options.ignore_protected_mode_settings = True
            options.ignore_zoom_level = True
            options.require_window_focus = True

            service = IeService(executable_path="./drivers/IEDriverServer.exe")
            return webdriver.Ie(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    @staticmethod
    def _create_remote_driver(browser_name, grid_url):
        common_args = ['--start-maximized']

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
        elif browser_name == "ie":
            options = webdriver.IeOptions()
            options.ignore_protected_mode_settings = True
            options.ignore_zoom_level = True
            options.require_window_focus = True
        else:
            raise ValueError(f"Unsupported browser for Grid: {browser_name}")

        if browser_name != "ie":
            for arg in common_args:
                options.add_argument(arg)

        options.set_capability("browserName",
                               "chrome" if browser_name == "chrome" else
                               "firefox" if browser_name == "firefox" else
                               "MicrosoftEdge" if browser_name == "edge" else
                               "internet explorer")
        options.set_capability("platformName", "windows")

        if browser_name == "ie":
            options.set_capability("se:ieOptions", {
                "ignoreProtectedModeSettings": True,
                "ignoreZoomSetting": True,
                "requireWindowFocus": True,
                "se:bidiEnabled": True
            })

        return webdriver.Remote(
            command_executor=grid_url,
            options=options
        )

    @staticmethod
    def create_driver(browser_name, use_grid=False, grid_url="http://localhost:4444/wd/hub"):
        browser_name = browser_name

        if use_grid:
            return DriverFactory._create_remote_driver(browser_name, grid_url)
        else:
            return DriverFactory._create_local_driver(browser_name)

