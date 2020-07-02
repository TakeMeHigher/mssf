from threading import Lock


class Singleton(type):
    lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls.lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance


class Foo(metaclass=Singleton):
    def __init__(self):
        pass


obj1 = Foo()
obj2 = Foo()

print(id(obj1) == id(obj2))
