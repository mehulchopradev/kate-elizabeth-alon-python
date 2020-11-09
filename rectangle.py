def area_rectangle(length, breadth):
    return length * breadth

def perimeter_rectangle(length, breadth):
    return 2 * (length + breadth)

# l1, b1 = 6, 4 # single line multi variable declaration
l1 = float(input('Enter length: ')) # l1 -> '5' -> 5.0
b1 = float(input('Enter breadth: ')) # b1 -> '3'
''' print(type(l1)) # str
print(type(b1)) ''' # str

a = area_rectangle(length=l1, breadth=b1)
p = perimeter_rectangle(length=l1, breadth=b1)

# Print the value of the variables a and p
'''
print() is one of the many built in functions
available in the python library
'''

print('Area is: ' + str(a))
print('Perimeter is : ' + str(p))
