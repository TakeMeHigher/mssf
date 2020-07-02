from threading import Lock


class Singleton(object):
    lock = Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(Singleton, cls).__new__(cls)

            return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(id(obj1) == id(obj2))
