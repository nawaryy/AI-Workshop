s = {11,22,11,33,44,22}
print(s) #unordered collection without duplicates
###
s1 = set() #empty set (otherwise it would be a dict)
s1.add(10)
s1.add(20)
print(s1)
###
s2={10,20,30,40}
print(len(s2))
s2.remove(30)
s2.discard(100) #wont give error if didnt find the item u mentioned.. its also used to delete the item
print(s2)
###UNION n INTERSECTION###
s3={1,2,3,4}
s4={3,4,5,6}
print(s3.union(s4))
print(s3.intersection(s4))
