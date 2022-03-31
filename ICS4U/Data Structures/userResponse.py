class UserResponse():
    def __init__(self, factors, name, grade):
        self.factors = factors
        self.name = name
        self.grade = grade
    def returnFactors(self):
      print(self.factors, self.name, self.grade)
