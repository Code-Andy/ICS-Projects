from userResponse import UserResponse


class StudentData(UserResponse):
    def __init__(self, dict):
        self.studentEmail = dict["studentEmail"]
        self.homeroomDep = dict["homeroomDep"]
        self.grade = dict["grade"]
        super().__init__(dict["factors"], dict["name"])

    def test(self):
        print(self.studentEmail, self.homeroomDep,
              self.factors, self.name, self.grade)
