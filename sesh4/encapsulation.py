#Encapsulation
class myClass:
    n = 10 #Public Variable
    _n = 100 #Protected Variable
    __n = 1000 #Private Variable

    def myfunc(self):
        print(self.__n)

obj = myClass()
print(obj.n)
print(obj._n)
#print(obj.__n) ERROR because private
obj.myfunc()