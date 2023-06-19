from core.api.models import SimpleStatus


class DetailedStatus(SimpleStatus):
    env: dict
