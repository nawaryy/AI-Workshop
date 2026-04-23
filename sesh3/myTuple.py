t = (1,2,64)
#t[2] = "hi" (u cannot change tuple cuz immutable)
print(t)

print(sum(t))
for item in t:
    print(item)
###
t1 = (10)
print(type(t1)) #gives int as a type, u need to add comma after the single item (10,)
#happens only in tuples