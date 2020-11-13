from com.abc.lib.student import Student

# list of books in the library
# every book, want to store title, price and pages

# a list of tuples
# element position 0 -> tuple
# element position 1 -> tuple

books = [
    ('Prog in java', 900, 4500),
    ('Prog in Python', 3400, 920),
    ('Scala programming', 4000, 560)
]
print(books)

# list of students in the college
# every student has name, gender, roll, marks

# a list of Student objects
# element position 0 -> Student
# element position 1 -> Student

students = [
    Student('mehul', 10, 'm', 90),
    Student('jane', 15, 'f', 98),
    Student('rock', 18, 'm', 65),
]
print(students)

# Gets a new list of the names of the male students from the students list.
males = [student.name for student in students if student.gender == 'm']
print(males)

'''
Create a matrix 2 x 2.
5   6
7   3
Represent this matrix in my python data structure
'''

'''
[
    (5 , 6),
    (7 , 3)
]
'''

'''
2D List
[
    [5, 6],
    [7, 3]
]
'''
