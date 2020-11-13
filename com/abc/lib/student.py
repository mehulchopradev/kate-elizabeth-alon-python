'''
For every class in python (built in or user defined), there is a single object (per class) created in the RAM.
Student class -> single object created in the RAM -> class object
'''
class Student:
    count = 0 # will be stored in the single class object of the class Student
    # these attributes are accesed using the class name

    # called during the object creation
    def __init__(self, name=None, roll=None, gender=None, marks=None):
        # constructor
        # self - current object (Student object)

        # initializes the attributes in the object
        self.name = name
        self.roll = roll
        self.gender = gender
        self.marks = marks

        Student.count += 1

    def create_student(name, roll, gender, marks):
        # it does not have self
        # class functions
        # called directly using the class name
        return Student(name=name, roll=roll, marks=marks, gender=gender)

    def get_details(self):
        # self - s1 Student object
        # self - s2 Student object
        # self - any Student object
        # instance functions
        ''' return 'Name: ' + self.name + '\nGender: ' + self.gender \
            + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks) '''
        # return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(self.name, self.gender, self.roll, self.marks)
        return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'.format(name=self.name, \
            gender=self.gender, roll=self.roll, marks=self.marks)

    def get_grade(self):
        # instance functions
        marks = self.marks
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

    def get_name_roll(self):
        return (self.name, self.roll)