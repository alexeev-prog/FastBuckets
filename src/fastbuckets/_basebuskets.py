from abc import ABC, abstractmethod
from typing import Any, List
from ._basebuskets import Task


class ABCBusket(ABC):
    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def validate(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def append_task(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_task(self, **kwargs) -> Task:
        raise NotImplementedError

    @abstractmethod
    def add_task_to_queue(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_task(self, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_task_from_queue(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def finish_task(self, task: Task) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def queue(self) -> List[Task]:
        raise NotImplementedError

    @property
    @abstractmethod
    def load_coeff(self) -> float:
        raise NotImplementedError
