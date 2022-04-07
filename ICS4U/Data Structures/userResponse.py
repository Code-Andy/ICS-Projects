from unicodedata import category


class UserResponse():
    def __init__(self, factors, name):
        self.factors = factors
        self.name = name

    def returnAll(self):
        print(f"User: {self.name} has a ")
        print(f"Stress factor is: {self.factors[0]}")
        print(f"Depression factor is: {self.factors[1]}")
        print(f"Anxiety factor is: {self.factors[2]}")
        print(f"Pessimism factor is: {self.factors[3]}")

    def userTrait(self):

        # 0-15 low, 15-35 is normal, 35<= is high
        # fix
        maxFactor = max(self.factors)
        minFactor = min(self.factors)

        if maxFactor <= 15:
            maxCon = "low"
        elif maxFactor > 15 or maxFactor <= 35:
            maxCon = "normal"
        elif maxFactor > 35:
            maxCon = "high"

        if minFactor <= 15:
            minCon = "low"
        elif minFactor > 15 or maxFactor <= 35:
            minCon = "normal"
        elif minFactor > 35:
            minCon = "high"

        print(
            f"User: {self.name} has {maxCon} amounts of {maxFactor} and {minCon} amounts of {minFactor}")
