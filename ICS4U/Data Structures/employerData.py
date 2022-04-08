from pkg_resources import require
from userResponse import UserResponse
import string


class EmployerData(UserResponse):
    def __init__(self, data, requires):
        self.employeeRequires = requires
        if len(str(data["employerId"])) == self.employeeRequires["maxDigits"]:
            self.employerId = data["employerId"]
        else:
            self.employerId = None
        if (data["department"]).casefold() in self.employeeRequires["department"]:
            self.department = data["department"]
        else:
            self.department = None
        super().__init__(data["factors"], data["name"])

    def employeeInfo(self):
        print(f"Employee id: {self.employerId}, Department: {self.department}")

    def changeDepartment(self, newDepartment):
        if newDepartment.casefold() in self.employeeRequires["department"]:
            self.department = (newDepartment.casefold()).capitalize()
        else:
            print("department does not exist")

    def removeEmployee(self, employeeDatabase):
        tempList = []
        for items in employeeDatabase:
            if items.employerId != self.employerId:
                tempList.append(items)

        return tempList

    def test(self):
        print(self.employerId, self.department, self.factors, self.name)
