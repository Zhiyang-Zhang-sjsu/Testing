from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def crawl_following_data(self, driver):
        pass
