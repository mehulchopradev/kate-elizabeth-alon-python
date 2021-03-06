# Library functions that help in student operations

def get_details(name, gender, roll, marks):
    return 'Name: ' + name + '\nGender: ' + gender + \
        '\nRoll: ' + str(roll) + '\nMarks: ' + str(marks)

def get_grade(marks):
    '''
    Scope of variables in Python is
    1. The entire file
    2. The enclosing function
    '''
    if marks > 100 or marks < 0:
        grade = 'Invalid'
    elif marks >= 70:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 40:
        grade  = 'C'
    else:
        grade = 'F'
    return grade