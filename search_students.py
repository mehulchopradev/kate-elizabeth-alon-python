from com.abc.lib.student import Student

# kind of a database
''' data = [
    Student('mehul', 10, 'm', 90),
    Student('jane', 15, 'f', 98),
    Student('rock', 18, 'm', 65),
] '''

data = {
    10: Student('mehul', 10, 'm', 90),
    15: Student('jane', 15, 'f', 98),
    18: Student('rock', 18, 'm', 65)
}

roll = int(input('Enter the roll to search: '))


''' for student in data:
    if student.roll == roll:
        print(student.get_details())
        break
else:
    # will execute whenever the corresponding for block is completely exhausted (looping done completely)
    # i.e. no break statement was encountered in the loop
    print('Student not found') '''

if roll in data:
    student = data[roll]
    print(student.get_details())
else:
    print('Student not found')
