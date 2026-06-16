from abc import ABC, abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def save_json(
        self,
        dataset: str,
        payload: dict,
    ) -> str:
        pass