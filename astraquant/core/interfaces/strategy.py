from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def on_candle(self, context):
        ...
