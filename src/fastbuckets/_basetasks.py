from abc import ABC, abstractmethod
from typing import Awaitable
from uuid import uuid5
from enum import Enum


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
        self.task_uuid: str = str(uuid5(short_name))
        self.state: TaskState = TaskState.WAITING

    def reload(self):
        self.state = TaskState.WAITING

    def is_finished(self):
        return True if self.state == TaskState.FINISHED else False

    def is_freezed(self):
        return True if self.state == TaskState.FREEZED else False

    def is_running(self):
        return True if self.state == TaskState.RUNNING else False

    def is_waiting(self):
        return True if self.state == TaskState.WAITING else False
