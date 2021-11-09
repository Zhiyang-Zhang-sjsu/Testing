import json

json_file = "./data/extracted_data/BBC News.json"

class GetBBCBreakingNewsData:
    def __init__(self, driver):
        self.__driver = driver

    def crawl_following_data(self):
        idx = "1"
        bbc_news = {}
        links = self.__driver.find_elements("xpath", "//*[@role='article']")
        json_fd = open(json_file, "w")
        for link in links:
            bbc_data = link.text.split("\n")
            bbc_news["article " + idx] = {}
            bbc_news["article " + idx]["Date"] = bbc_data[3]
            bbc_news["article " + idx]["News"] = " ".join(bbc_data[4 : -3])
            bbc_news["article " + idx]["Reply"] = bbc_data[-3]
            bbc_news["article " + idx]["Retweet"] = bbc_data[-2]
            bbc_news["article " + idx]["Like"] = bbc_data[-1]
            idx = str(int(idx) + 1)

        json.dump(bbc_news, json_fd)
