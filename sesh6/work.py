#List Comprehension
l = [10,20,30,40]
myl = []

for i in l:
    myl.append(i+2)

print("normal way: ", myl)


#simpler method:
lis = [x+2 for x in l]
print("Using comprehension: ", lis)

#print even no. from 1 - 10
even = [x for x in range(1,11) if x%2==0]
print("Even list: ", even)

#print 5 table using list comprehension
five = [x*5 for x in range(1,11)]
print(five)

#print X table without list comprehension
n = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n} X {i} = {i*n}")