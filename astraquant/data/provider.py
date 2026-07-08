from abc import ABC, abstractmethod

class DataProvider(ABC):
    @abstractmethod
    def load_spot(self):
        pass

    @abstractmethod
    def load_option(self):
        pass