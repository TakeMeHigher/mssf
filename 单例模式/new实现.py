from threading import Lock


class Singleton(object):
    lock = Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not hasattr(cls, "_instance"):
                cls._instance = object.__new__(cls)

            return cls._instance


class Child(Singleton):
    def __init__(self):
        Singleton.__init__(self)


obj1 = Singleton()
obj2 = Singleton()

print(id(obj1) == id(obj2))

ch1 = Child()
ch2 = Child()
print(id(ch1) == id(ch2))
