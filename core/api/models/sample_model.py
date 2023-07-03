from typing import Optional

from pydantic.main import BaseModel


class SampleModel(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    message: str
    creation_ts: Optional[int]
