import time
import random
import copy
from binarySearch import binarySearch
import dataGen

from insertionSort import insertionSort
from linearSearch import linearSearch


sizeLists = [5, 10, 100, 1000, 10000, 30000, 50000, 75000]


def runTimes(objectSize):
    insertionTimes = ""
    linearTimesUnsorted = ""
    linearTimesSorted = ""
    binaryTimes = ""
    for x in range(10):
        tempList = dataGen.generateData(objectSize)
        startTime = time.time()
        insertionSort(tempList)
        endTime = time.time()
        timeDif = endTime - startTime
        insertionTimes = insertionTimes + "," + timeDif

    for x in range(10):
        randomValue = random.randrange(0, objectSize)
        tempList = dataGen.generateData(objectSize, randomValue)
        startTime = time.time()
        linearSearch(tempList)
        endTime = time.time()
        timeDif = endTime - startTime
        linearTimesUnsorted = linearTimesUnsorted + "," + timeDif

    for x in range(10):
        randomValue = random.randrange(0, objectSize)
        tempList = dataGen.generateData(objectSize, randomValue)
        sortList = insertionSort(tempList)
        startTime = time.time()
        linearSearch(sortList)
        endTime = time.time()
        timeDif = endTime - startTime
        linearTimesSorted = linearTimesSorted + "," + timeDif


def main():

    startTime = time.time()
    endTime = time.time()

    print("\n\nThis took " + str(endTime - startTime) + " s")


insertionList = dataGen.generateData(100)

print(insertionList)
print(insertionSort(insertionList)[0:20])
print(insertionSort(insertionList)[-20:])

linearList = dataGen.generateSearchData(100, 50)
print(linearList)
print(linearSearch(linearList, 50))
print(linearSearch(insertionSort(linearList), 50))

binaryList = dataGen.generateSearchData(200, 21)
print(binaryList)
print(binarySearch(insertionSort(binaryList), 21))
