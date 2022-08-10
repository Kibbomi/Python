a = [1,2,3,4]
b = a  # reference.. not copy

print(a)
b.append(5) # a is updated
print(a) 


from copy import copy
c = [10,11,12,13]
d = copy(c)

c.append(6)
print(c)
print(d) # system allocates new memory for 'd'

