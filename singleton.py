def singleton(class_):
    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return wrapper


def another_singleton(_class):
    def wrapper(*args, **kwargs):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args, **kwargs))
        return getattr(_class, 'instance')

    return wrapper


@another_singleton
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@singleton
class Human1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


human_1 = Human('John', 20)
human_2 = Human('SecondName', 20)
human_3 = Human1('John', 20)
human_4 = Human1('SecondName', 20)

print(id(human_1))
print(id(human_2))
print(human_1.name)
print(human_2.name)
human_2.name = 'NewName'
print(human_1.name)
# True
# 1
