from com.abc.lib.student import Student

s1 = Student() # RAM (7009) -> Student object
s1.name = 'mehul chopra' # creates a name attribute in the s1 Student object
s1.roll = 10
s1.gender = 'm'
s1.marks = 90


s2 = Student() # RAM(7004) -> Student object
s2.name = 'jane' # creates a name attribute in the s1 Student object
s2.roll = 13
s2.gender = 'f'
s2.marks = 67

# print(s1)
# print(s2)

# access the attributes from an object
''' print(s1.name)
print(s1.gender)

print(s2.name)
print(s2.gender) '''

# print(s2.address) # will give an error as trying to access a non existent attribute from an object

print(s1.get_details())
# Python internally
# Student.get_details(s1)


print(s2.get_details())
# Python internally
# Student.get_details(s2)