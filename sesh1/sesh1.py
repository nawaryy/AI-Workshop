status = 200

match status:
    case 200:
        print("Success")

    case 404:
        print(:Page Not Found")
    case 500:
        print("Server Error")
    case _:
        print("invalud status code")
#####
a = 1000
if a = 1000:
    pass
else:
    print("hello")
#####
#non param , non return func
def myfunc():
    a=10
    b=13
    print("Hello meow")
    print(f"the sum is {a+b}")
myfunc()
#####
#non param, return func
def mysum():
    a=10
    b=20
    return a+b
res = mysum()
print(res)
print(mysum)
#####
#param, non return func
def myfu(a,b):
    print(a+b)
myfu(100,500)
#####
#param, return func
def myf(a,b):
    return(a+b)
print(myf(100,500))
#####
def myfo(x,y,z=100):
    return x+y+z
print(myfo(10,11)) #default value
print(myfo(10,11,10)) #update the value
#####
def greet(name = "Guest"):
    print(f"Hello {name}")
greet("Kelvin")
#####
#*args
def fonk(*numbers):
    return sum(numbers)
print(fonk(1,2,3,4,5,6,7,8,9,10))
#####
#**kwargs
def ff(**data):
    return data['name']
    return data['name'], data['age']
    return f"The name is {data['name']} and age is {data['age']}"
print(ff(name:"Alen",age:54))
#####