from abc import ABC, abstractmethod
from collections.abc import Awaitable
from enum import Enum
from time import time
from uuid import uuid5


class TaskState(Enum):
    WAITING = 0
    RUNNING = 1
    FREEZED = 2
    FINISHED = 3


class ABCTask(ABC):
    @abstractmethod
    def reload(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_finished(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_freezed(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_running(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_waiting(self) -> bool:
        raise NotImplementedError


class OneRunTask(ABCTask):
    def __init__(self, handler: Awaitable, short_name: str):
        self.handler: Awaitable = handler
        self.short_name: str = short_name
        self.task_uuid: str = str(uuid5(short_name + str(time())))
        self.state: TaskState = TaskState.WAITING

    def reload(self):
        self.state = TaskState.WAITING

    def is_finished(self):
        return self.state == TaskState.FINISHED

    def is_freezed(self):
        return self.state == TaskState.FREEZED

    def is_running(self):
        return self.state == TaskState.RUNNING

    def is_waiting(self):
        return self.state == TaskState.WAITING
