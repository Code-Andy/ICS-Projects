from userResponse import UserResponse


class StudentData(UserResponse):
    def __init__(self, data, requires):
        self.studentEmail = data["studentEmail"]
        self.homeroomDep = data["homeroomDep"]
        self.grade = data["grade"]
        super().__init__(data["factors"], data["name"])

    def test(self):
        print(self.studentEmail, self.homeroomDep,
              self.factors, self.name, self.grade)
