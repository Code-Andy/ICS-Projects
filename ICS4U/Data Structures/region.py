from userResponse import UserResponse


class Region(UserResponse):
    def __init__(self, studentEmail, school, factors, name, grade):
        self.studentEmail = studentEmail
        self.school = school
        super().__init__(factors, name, grade)

    def test(self):
        print(self.studentEmail, self.school,
              self.factors, self.name, self.grade)
