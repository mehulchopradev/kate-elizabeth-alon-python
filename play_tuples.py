# create a tuple of details of a book in library
b1 = ('Prog in C', 900, 4500)
print(type(b1))

# create an empty tuple
b2 = ()
print(type(b2))

# create a tuple that has only one element
b3 = ('Prog in Java',) # leave a trailing comma
print(type(b3))

# a tuple is also like a sequence of elements
# position of the elements is 0 based
print(b1[0])
print(b1[-1])

# extract a sub tuple (consiting of the price and pages) from the larger tuple
print(b1[1:])

# length of the tuple
print(len(b1))
print(len(b3))

# print on a new line, individual elements from the b1 tuple
for v in b1:
    print(v)

'''
A tuple is an immutable object
'''