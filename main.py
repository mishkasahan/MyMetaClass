class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print("Створено новий клас")
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMetaclass):
    pass

class MyClass1(metaclass=MyMetaclass):
    pass