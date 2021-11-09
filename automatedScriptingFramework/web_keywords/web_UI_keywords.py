from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from settings.browser_settings.chrome_options import ChromeOptions

TIMEOUT= 10
FREQUENCY = 0.5

class WebUIKeywords:
    def __init__(self, text, log):
        self.__driver = None
        if text.lower() == "chrome":
            self.__driver = webdriver.Chrome(options=ChromeOptions().options())
        else:
            try:
                self.__driver = getattr(webdriver, text)()
            except Exception as e:
                print(f"Exception: {e}")
                exit()

        self.__driver.implicitly_wait(TIMEOUT)
        self.log = log

    # visit a web site
    def visit(self, text):
        self.__driver.get(text)

    def click(self, by, value,):
        self.__element_wait_explicitly(by, value).click()

    def click_ignore_errors(self, by, value):
        try:
            self.__element_wait_explicitly(by, value).click()
        except:
            pass

    def input(self, by, value, text):
        self.__driver.find_element(by, value).send_keys(text)

    def input_ignore_errors(self, by, value, text):
        try:
            self.__driver.find_element(by, value).send_keys(text)
        except:
            pass

    def get_driver(self):
        return self.__driver

    def __element_wait_explicitly(self, by, value):
        return WebDriverWait(self.__driver, TIMEOUT, FREQUENCY).\
            until(lambda element: self.__driver.find_element(by, value),
                  message = "The element not found")

    def switch_to_handle(self, index = 1, close = False):
        handles = self.__driver.window_handles
        if close:
            self.__driver.close()
        self.__driver.switch_to.window(handles[index])

    # switch to Iframe
    def swith_to_frame(self, value, attribute = None):
        if attribute is None:
            self.__driver.switch_to.frame(value)
        else:
            self.__driver.switch_to.frame(self.__driver.find_element(attribute, value))

    def switch_to_default(self):
        self.__driver.switch_to.default_content()

    def quit(self):
        self.__driver.quit()

    def assert_text(self, by, value, expected_result):
        try:
            testing_result = self.__element_wait_explicitly(by, value).text
            assert expected_result == testing_result, f"Assertion fails: expected result - {expected_result}, testing result - {testing_result}!"
            return True
        except Exception as e:
            self.log.exception(f"Exception: {e}!")
            return False
