from __future__ import annotations

from abc import abstractmethod
from typing import Any

from utils import AbstractSingleton


class AbstractService(metaclass=AbstractSingleton):

    def __init__(self):
        pass

    @staticmethod
    def get() -> AbstractService:
        pass

    @abstractmethod
    def create(self, any_object: Any):
        pass

    @abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, any_object: Any):
        pass

    @abstractmethod
    def delete(self, identifier: Any):
        pass
