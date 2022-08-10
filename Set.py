
# init #
s = set()


# add #
s.add(1)
s.add(2)
s.add(5)
s.add(5)
s.add(123)
s.add("hello")
s.update([10,11,12])
print(s)

# remove #
s.remove(1)
s.remove(5)
# throw key error if remove the value not included in the set
print(s)






