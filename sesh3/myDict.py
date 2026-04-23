#d = {} #empty dict
#d = dict() #empty 

d = {"name":"Alen","age":"26"}
print(d)
print(len(d))
d["location"] = "doha"
print(d)
d["name"] = "Alen walker" #keys are special so u will get it overridden
print(d)
d["name1"] = "Bob"
print(d)
####
newd = {'name': 'Alen walker', 'age': '26', 'location': 'doha', 'name1': 'Bob'}
del newd["name1"] #deletes the complete item from dict
print(newd)
####
d4 = {"Country":"Qatar","mobile no":"12345678"}
newd.update(d4)
print(newd)
####
d5 = {'name': 'Alen walker', 'age': '26', 'location': 'doha', 'Country': 'Qatar', 'mobile no': '12345678'}
for item in d5:
   print(item) #gives the keys only
   print((item,d5[item]))
print(d5.keys())
print(d5.values())

for key,value in d5.items():
    print(key,value)

if "location" in d5.keys():
    d["location"] = "Al Gharafa"
else:
    print("not present")
    