from .college_user import CollegeUser

# Student IS-A CollegUser
# Student subclass of CollegeUser (super class)
# Student child class of CollegerUser (parent class)
class Student(CollegeUser):
    def __init__(self, name, roll, gender, marks):
        # self -> Student object -> 9000
        super().__init__(name, gender)
        # Internally
        # CollegeUser.__init__(self, name, gender)

        self.roll = roll
        self.marks = marks
    
    # method overriding
    def get_details(self):
        part1 = super().get_details()
        part2 = '\nRoll: {0}'.format(self.roll)

        return part1 + part2

    # own set of methods