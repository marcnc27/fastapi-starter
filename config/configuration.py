from utils import ThreadSafeSingletonMixins
import toml
import os


class Configuration(ThreadSafeSingletonMixins):

    def __init__(self):
        self.VERSION = toml.load("pyproject.toml")["tool"]["commitizen"]["version"]
        self.DEBUG = os.environ.get("DEBUG", "true").lower() == "true"
        self.PORT = int(os.environ.get("PORT", "5000"))
        self.POSTGRES_URL = os.environ.get("POSTGRES_URL", "localhost")
        self.POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", "5432"))
        self.POSTGRES_DB = os.environ.get("POSTGRES_DB", "sample")
        self.POSTGRES_TABLE = os.environ.get("POSTGRES_TABLE", "sample-table")
        self.POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
        self.POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "mysecretpassword")

    @staticmethod
    def get():
        return Configuration()

    def as_dict(self):
        env = vars(self)
        if "get_uuid" in env:
            del env["get_uuid"]
        return env
