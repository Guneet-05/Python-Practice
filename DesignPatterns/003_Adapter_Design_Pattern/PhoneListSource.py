from abc import ABC,abstractmethod

# Interface PhoneListSource
class PhoneListSource(ABC):
    @abstractmethod
    def getPhoneNumbers():
        pass