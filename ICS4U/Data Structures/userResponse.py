class UserResponse():
    def __init__(self, factors, name):
        self.factors = factors
        self.name = name

    def returnValues(self):
        print(self.factors, self.name)

    def returnFactors(self):
        print(f"Your stress factor is: {self.factors[0]}")
        print(f"Your depression factor is: {self.factors[1]}")
        print(f"Your anxiety factor is: {self.factors[2]}")
        print(f"Your pessimism factor is: {self.factors[3]}")
