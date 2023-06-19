from pydantic.main import BaseModel


class SimpleStatus(BaseModel):
    status: str
