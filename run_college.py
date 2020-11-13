from com.abc.college.student import Student
from com.abc.college.professor import Professor

s1 = Student('mehul', 10, 'm', 45)
'''
1. RAM (9000) - Student object
2. Student.__init__(9000, 'mehul', 10, 'm', 45)
'''

p1 = Professor('jane', 'f', ['Physics', 'Chemistry'])
'''
1. RAM (5600) - Professor object
2. Professor.__init__(5600, 'jane', 'f', ['Physics', 'Chemistry'])
'''

''' print(s1.name)
print(s1.gender)
print(s1.roll)

print(p1.name)
print(p1.gender)
print(p1.subjects) '''

print(s1.get_details())
# Internally
# Student.get_details(s1)


print(p1.get_details())
# Internally
# Professor.get_details(p1)