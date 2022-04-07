from userResponse import UserResponse


class EmployerData(UserResponse):
    def __init__(self, dict):
        self.employerId = dict["employerId"]
        self.department = dict["department"]
        super().__init__(dict["factors"], dict["name"])

    def test(self):
        print(self.employerId, self.department, self.factors, self.name)
