#1. Single Level Inheritance:
class Parent:
    def psdisplay(self):
        print("This is parent property")

class Child(Parent): #inhertis from Parent
    def cdisplay(self):
        print("This is child property")


c = Child() #creating object of the child
c.cdisplay()
c.psdisplay()
print("---------------")

#2.Multilevel Inheritance:
class grandChild(Child):
    print("This is grandchild property")

g = grandChild()
g.cdisplay()
g.psdisplay()
print("---------------")

#3. Multiple Inheritance:
class Father:
    def fdisplay(self):
        print("This is father property")
    
class Mother:
    def mdisplay(self):
        print("This is mother property")

class Son(Mother, Father): #inherits from 2 independant classes
    def sdisplay(self):
        print("This is son property")

s = Son()
s.sdisplay()
s.mdisplay()
s.fdisplay()
print("---------------")

#4. Hierarchical Inheritance (Hybrid)
class Papa:
    def padisplay(self):
        print("Papa property")

class Child1(Papa): #inherit from Papa
    def c1display(self):
        print("c1 property")
    
class Child2(Papa): #inherit from Papa
    def c2display(self):
        print("c2 property")

c1 = Child1()
c1.padisplay()
c2 = Child2()
c2.padisplay()