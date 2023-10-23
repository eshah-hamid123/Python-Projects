class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


person1 = Person("Eisha")
print(person1.get_name())
