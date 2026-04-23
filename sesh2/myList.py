l = [10,"hello",3.14,[11,22,33],{1,2,3},(10,20,30)]
print(len(l)) #get 6
print(l[3][1]) #get 22
print(l[5][2]) #get 30

l = [] #empty list
print(type(l)) #get <'class list'>
myl = list()
print(type(myl)) #get <'class list'>

l1 = []
l1.append(10)
print(l1) #get [10]
l1.append(20)
l1.append(30)
print(l1) #get [10,20,30]  .. it appends in last position
l1.insert(15,1) #insert 15 at position 1 (specific place)
print(l1) #get [10,15,20,30]
l1.extend([11,22,33]) #add it to the end
print(l1) #get [10,15,20,30,11,22,33]

#insert 1 to 10 except 2 and 5
l2 = []
for i in range(1,11):
    if i==2 or i==5:
        continue
    l2.append(i)
print(l2) #gives [1,3,4,6,7,8,9,10]

#even numbers from 1 to 10
l3 = []
for i in range(1,21):
    if i%2 == 0: #for odd numbers put i%2!=0
        l3.append(i)
print(l3) #gives [2,4,6,8,10,12,14,16,18,20]

#membership: in, not in (linear search)
fruits = ["apple","mango","banana","grapes"]
is_fruit_found =  False #flag
for fruit in fruits:
    if fruit == "mango":
        is_fruit_found = True

if is_fruit_found == True:
    print("found")
else:
    print("not found")

print("grapes" in fruits) #you get true.. this is Membership - uses linear search 
print("grapes" not in fruits) #get false
print("kiwi" in fruits) #get false

####
l3 = [11,22,33,44]
l3.remove(33) #removes 33
l3.pop(1) #removes 22
l3.pop() #by default removes the last item
print(l3)

l4 = [11,22,33,44]
l4.clear() #clears the whole list 
print(l4) 
del l4 #delete from the memory
#print(l4) #gives error
####
l5 = [1,2,3,4,5]
print(l5[-1]) #prints [5]
l5.reverse() #reverses the list
print(l5) #[5,4,3,2,1]

for i in range(5,0,-1): #print in reverse order (start,end,step)
    print(i) #5 4 3 2 1 

l6=[10,20,30,40]
myli = []
for i in range(len(l)-1,-1,-1):
    myli.append(l6[i])
print(myli) #40 30 20 10
print(l6[::-1]) #slicing technique - 40 30 20 10
####
l7=[5,4,1,2]
l7.sort()
print(l7) # prints [1,2,4,5]
output = sorted(l)
print(output) # prints [1,2,4,5]
####
l8=[5,4,1,2]
print(max(l8))
print(min(l8))
print(sum(l8))
####
#remove the redundant items from the list
l9 = [93,44,5,44,6,11] 
ltemp = []
for item in l9:
    if item not in ltemp:
        ltemp.append(item)
print(ltemp) #[3,44,5,6,11]
 #theres more