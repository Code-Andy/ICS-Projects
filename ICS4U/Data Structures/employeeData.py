
from userResponse import UserResponse


class EmployerData(UserResponse):
    """
    Employer data class inherited from userResponse  

    Attr:
        employeeId (string): Employee's Id
        department (string): Employee's department
        factors (list) : Employee's Mental Health Factors
        name (string) Employee's Name

    Methods:
        returnAll() -> str
            Returns user infomation
        sumOfFactors() -> str
            Returns sum of all factors
        userTrait() -> str
            Returns string containing user's best and worst factors
        employeeInfo() -> str
            Returns employee's info data as one string
        changeDepartment() -> void
            Allow user to change departments 
        removeEmployee() -> str
            Allows employee to remove themselves

    Args:
        UserResponse (class): An employer's sample response layout
    """

    def __init__(self, data, requires):
        """
        Initializes the class with given parameters stored as self variables

        Args:
            data (dict): Data from json input
            requires (dict): Constraints set by user in main.py for the classes variables

        Compares the values from the json input to the requires values
        If the values are correct, it is stored as a class variable
        If not, it is set to None
        It then passes the rest of the data to the parent class's initialization function
        """
        self.employeeRequires = requires
        if len(str(data["employerId"])) == self.employeeRequires["maxDigits"]:
            self.employerId = int(data["employerId"])
        else:
            self.employerId = None
        if (data["department"]).casefold() in self.employeeRequires["department"]:
            self.department = data["department"]
        else:
            self.department = None
        super().__init__(data["factors"], data["name"])

    def employeeInfo(self):
        """
        Returns employee's info data as one string
        """
        return(
            f"Employee {self.name} with id: {self.employerId} is from {self.department}")

    def changeDepartment(self, newDepartment):
        """
        Change departments 

        Args:
            newDepartment (string): New department the employee is trying to change to

        Again checks if new department is in the requires
        Otherwise a simple error message would be printed
        """
        if newDepartment.casefold() in self.employeeRequires["department"]:
            self.department = (newDepartment.casefold()).capitalize()
        else:
            print("Error : Invalid Department")

    def removeEmployee(self, employeeDatabase):
        """
        Remove employee

        Args:
            employeeDatabase (list): List of employee objects

        Returns:
            list: modified list without the employee's own data
        """
        tempList = []
        for items in employeeDatabase:
            if items.employerId != self.employerId:
                tempList.append(items)
        return tempList
