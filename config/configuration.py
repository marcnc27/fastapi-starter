from utils import ThreadSafeSingletonMixins
import toml
import os


class Configuration(ThreadSafeSingletonMixins):

    def __init__(self):
        self.VERSION = toml.load('pyproject.toml')['tool']['commitizen']['version']
        self.DEBUG = os.environ.get('DEBUG', 'true').lower() == 'true'
        self.PORT = int(os.environ.get('PORT', '5000'))

    @staticmethod
    def get():
        return Configuration()

    def as_dict(self):
        env = vars(self)
        if 'get_uuid' in env:
            del env['get_uuid']
        return env
