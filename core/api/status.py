from fastapi import APIRouter

from constants import status_path, status_detailed_path
from core.api.models import SimpleStatus, DetailedStatus
from core.api.services import StatusService
from utils import Logger

logger = Logger.get_logger(__name__)

status_router = APIRouter()


@status_router.get(path=status_path, status_code=200, response_model=SimpleStatus)
def get_simple_status():
    return StatusService.get().read(simple=True)


@status_router.get(path=status_detailed_path, status_code=200, response_model=DetailedStatus)
def get_detailed_status():
    return StatusService.get().read(simple=False)
