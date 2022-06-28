s1 = {1,2,3}
s2 = {9,8,7}
print(s1)

#functions
s1.add(4)
s1.pop()
s1.remove(3)
s2.discard(7)

#insert s1 elements to s2
s2.update(s1)

#union
print(s1|s2)
print(s1.union(s2))

#intersection
print(s1 & s1)
print(s1.intersection(s2))

#difference
print(s1-s2)
print(s1.difference(s2))
