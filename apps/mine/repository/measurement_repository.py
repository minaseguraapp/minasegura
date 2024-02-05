from abc import ABC, abstractmethod


class IMeasurementRepository(ABC):
    @abstractmethod
    def save(self, measurement):
        raise NotImplementedError

    # @abstractmethod
    # def find_all(self):
    #     raise NotImplementedError

    @abstractmethod
    def find_by_mine(self, mine_id, zone_id, type_name):
        raise NotImplementedError

    # @abstractmethod
    # def find_by_id(self, id: str):
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def delete_by_id(self, id: str):
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def update_by_id(self, id: str, measurement):
    #     raise NotImplementedError
