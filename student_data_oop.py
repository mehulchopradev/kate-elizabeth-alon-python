from com.abc.lib.student import Student

print(Student.count)

s1 = Student('mehul chopra', 10, 'm', 45) # RAM (7009) -> Student object
print(s1.name)
print(s1.roll)
'''
Internally
1. In the RAM at some random memory address (7009) it is going to reserve some space for this Student object
2. Student.__init__(7009)
'''

''' s1.name = 'mehul chopra' # creates a name attribute in the s1 Student object
s1.roll = 10
s1.gender = 'm'
s1.marks = 45 '''


s2 = Student(name='jane', roll=13, marks=67, gender='f') # RAM(7004) -> Student object
print(s2.name)
print(s2.roll)

print(Student.count)

''' s2.name = 'jane' # creates a name attribute in the s1 Student object
s2.roll = 13
s2.gender = 'f'
s2.marks = 67 '''

# print(s1)
# print(s2)

s3 = Student(gender='m', marks=90, roll=14, name='rock')
print(s3.name)
print(s3.roll)

''' s3.student_name = 'rock'
s3.r = 14
s3.gen = 'm'
s3.marks = 90 '''

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

print(s3.get_details())

print(s1.get_grade())
# Internally
# print(Student.get_grade(s1))

print(s2.get_grade())

s4 = Student()
'''
1. RAM 9009 reserve space for the student object
2. Student.__init__(9009)
'''

print(Student.count)

# calling a class function
s5 = Student.create_student(name='jane', gender='f', marks=90, roll=45)
print(s5.get_details())
print(s5.get_grade())

t = s5.get_name_roll() # t -> tuple
''' name = t[0]
roll = t[1] '''

name, roll = t # tuple unpacking
print(name)
print(roll)