from abc import ABC, abstractmethod

class Broker(ABC):
    @abstractmethod
    def historical(self,*args,**kwargs):
        ...
