from threading import Lock


class Singleton(object):
    _lock = Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        with cls._lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = Singleton()

            return Singleton._instance


obj1 = Singleton.instance()
obj2 = Singleton.instance()

print(id(obj1) == id(obj2))
