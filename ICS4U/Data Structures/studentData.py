from userResponse import UserResponse


class StudentData(UserResponse):
    def __init__(self, dict):
        self.studentEmail = dict["studentEmail"]
        self.school = dict["school"]
        self.grade = dict["grade"]
        super().__init__(dict["factors"], dict["name"])

    def test(self):
        print(self.studentEmail, self.school,
              self.factors, self.name, self.grade)
