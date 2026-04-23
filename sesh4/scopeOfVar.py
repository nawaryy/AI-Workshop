g_name = "Khalid" #Global Variable

class Student:
    c_name = "Zain" #Class Variable or Instance Variable

    def __init__(self): #super method - constructor
        self.i_name = "Hasan" #Instance Variable

    def myfunc(self):
        l_name = "Sara" #Local Variable
        print(g_name)
        print(self.c_name)
        print(self.i_name)
        print(l_name)
s1 = Student()
s1.myfunc()
print(s1.c_name)
print(s1.i_name)