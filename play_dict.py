# empty dict in python
et = {}

# create a dict with some student data
student = { 12: ('mehul', 'm'), 7: ('jane', 'f'), 15: ('jill', 'f') }
print(student)
print(type(student))

# update the data of student with roll 15
student[15] = ('mike', 'm')

print(student)

# add a new student in the dict
student[20] = ('jill', 'f')

print(student)

# get the details of the student whose roll no is 7
print(student[7])

# student[89] # this gives an error

# `in` membership operator to check whether a key exists in the dict or no
print(89 in student)
print(7 in student)

# dict represents a sequence of elements
for v in student:
    print(v) # key from the dictionary

items = student.items()
# [(12, ('mehul', 'm')), (7, ('jane', 'f')), (15, ('mike', 'm')), (20, ('jill', 'f'))]

for item in items:
    # item -> (12, ('mehul', 'm'))
    print('Name: ' + item[1][0])
    print('Roll: ' + str(item[0]))

print(student.keys())
print(student.values())

# remove a student whose role number is 15, from the dict
del student[15]

print(student)