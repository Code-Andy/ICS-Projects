class UserResponse():
    """
    Parent class of mock user responses for summative project
    Attr:
        factors (list) : Mental Health Factors
        name (string) : Name

    Methods:
        returnAll() -> str
            Returns user infomation
        sumOfFactors() -> str
            Returns sum of all factors
        userTrait() -> str
            Returns string containing user's best and worst factors
    """

    def __init__(self, factors, name):
        """
        Initializes the class with given parameters stored as self variables

        Args:
            factors (list): List containing 4 mental health factors gauged by our survey
            name (string): User's response name
        """
        self.factors = factors
        self.name = name

    def returnAll(self):
        """
        Returns user infomation as multiline string
        """
        outputString = []
        outputString.append(f"User: {self.name} has a ")
        outputString.append(f"Stress factor is: {self.factors[0]}")
        outputString.append(f"Depression factor is: {self.factors[1]}")
        outputString.append(f"Anxiety factor is: {self.factors[2]}")
        outputString.append(f"Pessimism factor is: {self.factors[3]}")
        outputString = '\n'.join(outputString)
        return(outputString)

    def sumOfFactors(self):
        """
        Returns sum of all factors
        """
        sum = 0
        for values in self.factors:
            sum += values
        sum = int(sum/4)
        return(sum)

    def userTrait(self):
        """
        Returns string containing user's best and worst factors
        """

        maxFactor = max(self.factors)
        minFactor = min(self.factors)

        traitList = ["stress", "depression", "anxiety", "pessimism"]

        if maxFactor <= 15:
            maxCon = "low"
        elif maxFactor > 15 and maxFactor <= 35:
            maxCon = "normal"
        elif maxFactor > 35:
            maxCon = "high"

        if minFactor <= 15:
            minCon = "low"
        elif minFactor > 15 and maxFactor <= 35:
            minCon = "normal"
        elif minFactor > 35:
            minCon = "high"

        return(str(
            f"User: {self.name} has {maxCon} amounts of {traitList[self.factors.index(maxFactor)]} and {minCon} amounts of {traitList[self.factors.index(minFactor)]}"))
