from abc import ABC, abstractmethod


class IAlertRepository(ABC):
    @abstractmethod
    def save(self, alert):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError
