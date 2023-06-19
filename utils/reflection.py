import threading
from abc import ABCMeta
from uuid import uuid4


class SingletonMetaclass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super()
            instance.__setattr__('uuid', f'{uuid4()}')
            instance = instance.__call__(*args, **kwargs)
            instance.get_uuid = lambda: instance.uuid
            cls._instances[cls] = instance

        return cls._instances[cls]


class ThreadSafeSingletonMixins(object):
    __lock = threading.Lock()
    __instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls.__call__(*args, **kwargs)
        return cls.__instance


class AbstractSingleton(ABCMeta):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super()
            instance.__setattr__('uuid', f'{uuid4()}')
            instance = instance.__call__(*args, **kwargs)
            instance.get_uuid = lambda: instance.uuid
            cls.__instances[cls] = instance

        return cls.__instances[cls]
