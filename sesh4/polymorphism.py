#Polymorphism in 2 ways: Overloading & Overriding

#--OVERLOADING:--
#1- Operator Overload
print(10+20) #operands are 10 and 20 (+)
print("Hi"+"Hello") #contacinating strings (+)

print(10 * 2) #multiplication (*)
l = [1,2,3]
print(l * 2) #replication (*)

#2- Method Overload (doing same thing but in different ways)
def add(): #summation
    print(10+1000)
add()

def add(a,b): #summation
    print(a+b)
add(100,20)

def add(a,b=10): #summation
    print(a+b)
add(10)

#--OVERRIDING:--
class Parent:
    def display(self):
        print("Parent property")
    
class Child(Parent):
    def myparent(self):
          super().display()
    def display(self):
        print("Child property")

c = Child()
c.display() #will print the child's display since it prioritizes it 
c.myparent() #will print the parent's display cuz we used "super"