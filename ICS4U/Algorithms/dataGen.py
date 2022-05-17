import random


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return("(x: " + str(self.x) + ", " + "y: " + str(self.y) + ")")

    def __repr__(self):
        return str(self)


def generateData(size):
    newList = []
    for i in range(size):
        x = round(random.random()*size)
        y = round(random.random()*size)
        newCoord = Coord(x, y)
        newList.append(newCoord)
    return newList


def generateSearchData(size, target):
    newList = []
    for i in range(size):
        x = round(random.random()*size)
        y = round(random.random()*size)
        newCoord = Coord(x, y)
        newList.append(newCoord)
    newList[random.randrange(size)].x = target
    return newList
