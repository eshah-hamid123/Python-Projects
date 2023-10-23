from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def task(self):
        print('Abstract task here')


class TestClass(AbstractClass):
    def task(self):
        print('Test class it is!')


testclass = TestClass()
testclass.task()
# ab = AbstractClass()
# ab.task()