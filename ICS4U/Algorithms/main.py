import random
import dataGen

from timeit import timeit
from insertionSort import insertionSort
from linearSearch import linearSearch
from binarySearch import binarySearch

# Imports of algorithms and timeit function to measure time usage

sizeLists = [5, 10, 100, 1000, 10000, 30000, 50000, 75000]

# Object size list we're evaluating


def runTimes(objectSize):
    insertionTimes = ""
    linearTimesUnsorted = ""
    linearTimesSorted = ""
    binaryTimes = ""

    for x in range(10):
        randomValue = random.randrange(0, objectSize)
        tempList = dataGen.generateSearchData(objectSize, randomValue)

        timeDif = timeit(lambda: linearSearch(
            tempList, randomValue), number=1)
        linearTimesUnsorted = linearTimesUnsorted + "," + str(timeDif)

        print(f"linear {x}")

        timeDif = timeit(lambda: insertionSort(tempList), number=1)
        insertionTimes = insertionTimes + "," + str(timeDif)

        print(f"insertion {x}")

        timeDif = timeit(lambda: linearSearch(
            tempList, randomValue), number=1)
        linearTimesSorted = linearTimesSorted + "," + str(timeDif)

        print(f"sortedlinear {x}")

        timeDif = timeit(lambda: binarySearch(
            tempList, randomValue), number=1)
        binaryTimes = binaryTimes + "," + str(timeDif)

        print(f"binary {x}")

    insertionTimes = insertionTimes[1:]
    linearTimesUnsorted = linearTimesUnsorted[1:]
    linearTimesSorted = linearTimesSorted[1:]
    binaryTimes = binaryTimes[1:]

    # Removing first comma from runtime strings

    f.write(f"{objectSize} objects\n")
    f.write(f"{insertionTimes}\n")
    f.write(f"{linearTimesUnsorted}\n")
    f.write(f"{linearTimesSorted}\n")
    f.write(f"{binaryTimes}\n")
    f.write("\n")

    # Saving runtimes to text file


with open('newtimes.txt', 'w') as f:
    for items in sizeLists:
        print(items)
        runTimes(items)

# Runtimes graphs via google sheets : https://docs.google.com/spreadsheets/d/1Yb1b97q9YA2JUf0KuyzPd3IADyBdS2xNJmZLbSoA6BI/edit?usp=sharing

# Demo of working sorts and printing first and last 20 elements in insertionSort()

# insertionList = dataGen.generateData(100)

# print(insertionList)
# print(insertionSort(insertionList)[0:20])
# print(insertionSort(insertionList)[-20:])

# linearList = dataGen.generateSearchData(100, 50)
# print(linearList)
# print(linearSearch(linearList, 50))
# print(linearSearch(insertionSort(linearList), 50))

# binaryList = dataGen.generateSearchData(200, 21)
# print(binaryList)
# print(binarySearch(insertionSort(binaryList), 21))
