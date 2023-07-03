from typing import List

from fastapi import APIRouter

from constants import version_path, api_path
from core.api.models import SampleModel
from core.api.services import SampleService

sample_router = APIRouter()


@sample_router.get(path=f'/{api_path}/{version_path}/sample', status_code=200, tags=['Sample service'],
                   response_model=List[SampleModel])
def get_samples() -> List[SampleModel]:
    return SampleService.get().read()
