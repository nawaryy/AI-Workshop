from abc import ABC, abstractmethod #need to import ABC (abstract class) and abstract method

class myAbstractClass(ABC): #inheriting from the library so it becomes an abstract class
    @abstractmethod #mandatory
    def myabstractmethod(self): #a method which is declared but not defined
        pass

class myConcreteClass(myAbstractClass): #inherit the abstract class
    def myabstractmethod(self):
        print("hello!!")

obj = myConcreteClass()
obj.myabstractmethod()