# set of fruits
fruits = {'banana', 'apple', 'chicku', 'apple'}
print(fruits)
print(type(fruits))

# add a new element in the set
fruits.add('grapes')
print(fruits)

fruits.add('grapes') # does not given an error
print(fruits) # but does not add in the set

# remove an element from the list
fruits.remove('apple')
print(fruits)

# whether there is banana in the set or no
print('banana' in fruits)

# length of the set
print(len(fruits))

# a set represents a sequence of elements
for fruit in fruits:
    print(fruit)

# print(fruits[0]) # this will not work

# empty set
# es = {} # do not do in this way as it would create a dict
es = set()
print(type(es))