class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, new_age):
        self.age = new_age
        return self

    def set_name(self, new_name):
        self.name = new_name
        return self

if __name__ == '__main__':
    h1 = Human("John", 20)
    h1.set_name("NewName")
    h1.set_age(25)
    print(h1.name)
    print(h1.age)
    h1.set_name("NewName2").set_age(80)
    print(h1.name)
    print(h1.age)