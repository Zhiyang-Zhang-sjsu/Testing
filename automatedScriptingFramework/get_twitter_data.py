import os
import sys

from followings.get_bbc_breaking_news_data import GetBBCBreakingNewsData
from settings.log_settings import log_conf
from excel_driver.execl_test_data_management import ExeclTestDataManagement

TEST_CASE_FILE_EXTENTION = ".xlsx"
TEST_CASE_DIR = "data/test_data/excel"
LOG_SETTING_FILE = "./settings/log_settings/log.ini"
FOLLOWING_CLASSES = {
    "BBC Breaking News" : "GetBBCBreakingNewsData"
}

class GetFollowingsDataOnTwitter:
    def __init__(self, driver):
        self.__driver = driver
        self.__strategy = None

    def get_driver(self):
        return self.__driver

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def get_following_data(self):
        self.__strategy.crawl_following_data()

    def string_to_class(self, string):
        return getattr(sys.modules[__name__], string)

if __name__ == "__main__":
    log = log_conf.get_log(LOG_SETTING_FILE)
    drivers = {}
    for path, direcotry, files in os.walk(TEST_CASE_DIR):
        for file in files:
            file_name, file_type = os.path.splitext(file)
            if file_type == TEST_CASE_FILE_EXTENTION:
                if "deprecated" not in file_name:
                    log.info(f"Test case: {file_name} is running")
                    execl_test_data_management = ExeclTestDataManagement()
                    driver = execl_test_data_management.run_test_data(path + "/" + file, log)
                    drivers.update(driver)
                else:
                    log.info("Only supports excel files for test cases")

    for following, following_driver in drivers.items():
        if following_driver == None:
            continue

        log.info(f"Getting {following} data!")
        following_on_twitter = GetFollowingsDataOnTwitter(drivers[following])
        following_data = following_on_twitter.string_to_class(FOLLOWING_CLASSES[following])(following_on_twitter.get_driver())
        following_on_twitter.set_strategy(following_data)
        following_on_twitter.get_following_data()
        following_on_twitter.get_driver().quit()
        log.info(f"{following} data extracted!")