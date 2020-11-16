# object is a built in class in the python library
# every class in python implicitly inherits from the class object
class CollegeUser(object):
    def __init__(self, name, gender):
        # self - Student object - 9000
        # self - Professor object - 5600
        # self - sub class object of CollegeUser
        self.name = name
        self.gender = gender

    def get_details(self):
        # self - Student object
        # self - Professor object
        # self - subclass object to CollegeUser
        return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)

    def __str__(self):
        return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)