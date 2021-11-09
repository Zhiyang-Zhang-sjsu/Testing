from selenium import webdriver

class ChromeOptions:
    def options(self):
        options = webdriver.ChromeOptions()

        # maximize window
        options.add_argument("start-maximized")

        # suppress warnings
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

        # disable password pop-up
        prefs = {}
        prefs["credentials-enable-service"] = False
        prefs["profile.password_manager_enable"] = False
        options.add_experimental_option("prefs", prefs)

        return options
