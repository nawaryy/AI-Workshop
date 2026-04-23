name = "alen" #normal variable
class School: #class name should start with capital letter for clean code
    #constuctor (single constructor per class)
    def __init__(self, sc_name):
        self.sc_name = sc_name
    #instance variable
    school_name = "Qatar School" #instance variable (variable created inside the class)
    #function/method
    def student_details(self): #must write "self" if its a function inside the class, otherwise not needed
        #self is a default argument that calls to itself
        print("this is a function")
    def student_det(self,name,grade):
        print(f"The name of the student is {name} and the grade is {grade} and the school name is {self.school_name}")
        #name and grade are local variables
#obj = School() #object
#print(obj.school_name)
#obj.student_details()
#obj2 = School()
#obj2.student_details()

s1 = School()
s1.student_det("Mohammed","A")
s2 = School()
s2.student_det("Zain","B")

S1 = School("doha school")
S1.student_det("Hamed","A")