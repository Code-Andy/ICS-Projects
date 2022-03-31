"""
Given a array of numbers, and a single number n, return an
extracted array of unique numbers that are
evenly divisible by n. Your extracted array should be
sorted in ascending numerical order.

Examples:
If you ran extractEvenlyDivisible([1,2,3,4,5,6,7,8,9], 3) you would get a return value of [3,6,9].
If you ran extractEvenlyDivisible([1,9,3,4,3,6,7,8,9], 3) you would get a return value of [3,6,9].
"""

a = [1, 9, 3, 4, 3, 6, 7, 8, 9, 5, 6, 3, 12, 24, 66, 33]


def extractEvenlyDivisible(array, divisor):
    def helper(arr, index):
        if(len(arr) == index + 1):
            return arr
        elif ((arr[index] % divisor) == 0):
            return helper(arr, index + 1)
        else:
            arr.pop(index)
            return helper(arr, index)
    return sorted(set(helper(array, 0)))


print(extractEvenlyDivisible(a, 3))
