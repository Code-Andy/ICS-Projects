from userResponse import UserResponse


class StudentData(UserResponse):
    """Student data class inherited from userResponse  

    Args:
        UserResponse (class): An student's sample response layout
    """

    def __init__(self, data, requires):
        """Initializes the class with given parameters stored as self variables


        Args:
            data (dict): data from json input
            requires (dict): constraints set by user in main.py for the classes variables

            Compares the values from the json input to the requires values
            If the values are correct, it is stored as a class variable
            If not, it is set to None
            It then passes the rest of the data to the parent class's initialization function
        """
        self.studentRequires = requires

        splitEmail = data["studentEmail"].split("@")

        if len(splitEmail[0]) <= self.studentRequires["maxDigits"] and splitEmail[1] == self.studentRequires["domain"]:
            self.studentEmail = data["studentEmail"]
        else:
            self.studentEmail = None

        if (data["homeroomDep"]).casefold() in self.studentRequires["department"]:
            self.homeroomDep = data["homeroomDep"]
        else:
            self.homeroomDep = None

        self.grade = data["grade"]

        super().__init__(data["factors"], data["name"])

    def studentInfo(self):
        """Returns students's info data as one string
        """
        return(
            f"Student: {self.name} with email address: {self.studentEmail} is from a {self.homeroomDep} homeroom")

    def changeHomeroom(self, newHomeroom):
        """Change homerooms

        Args:
            newHomeroom (string): Student's new homeroom

        Again checks if new homeroom is in the requires
        Otherwise a simple error message would be printed
        """
        if newHomeroom.casefold() in self.studentRequires["department"]:
            self.homeroomDep = (newHomeroom.casefold()).capitalize()
        else:
            print("Error : Invalid Homeroom")

    def removeStudent(self, studentDatabase):
        """Remove student

        Args:
            studentDatabase (list): list of student objects

        Returns:
            list: modified list without the student's own data
        """
        tempList = []
        for items in studentDatabase:
            if items.studentEmail != self.studentEmail:
                tempList.append(items)
        return tempList
