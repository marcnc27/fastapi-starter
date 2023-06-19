from __future__ import annotations

from typing import Any

from config import Configuration
from core.api.models import SimpleStatus, DetailedStatus
from core.api.services import AbstractService
from utils import Logger

logger = Logger.get_logger(__name__)


class StatusService(AbstractService):

    def create(self, any_object: Any):
        raise NotImplementedError()

    def read(self, simple: bool):
        configuration = Configuration.get()
        if configuration.DEBUG:
            logger.debug('reading status from service')
        if simple:
            return SimpleStatus(status='on')
        return DetailedStatus(status='on', env=Configuration.get().as_dict())

    def update(self, any_object: Any):
        raise NotImplementedError()

    def delete(self, identifier: Any):
        raise NotImplementedError()

    @staticmethod
    def get() -> StatusService:
        return StatusService()
