from .college_user import CollegeUser

# Professor IS-A CollegeUser
class Professor(CollegeUser):
    def __init__(self, name, gender, subjects):
        # self - Professor object - 5600
        super().__init__(name, gender)
        # CollegeUser.__init__(self, name, gender)
        self.subjects = subjects