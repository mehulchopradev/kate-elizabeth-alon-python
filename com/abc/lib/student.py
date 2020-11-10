class Student:
    def get_details(self):
        # self - s1 Student object
        # self - s2 Student object
        # self - any Student object
        return 'Name: ' + self.name + '\nGender: ' + self.gender \
            + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks)