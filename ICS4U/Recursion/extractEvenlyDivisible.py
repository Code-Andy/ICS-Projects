"""
Given a array of numbers, and a single number n, return an
extracted array of unique numbers that are
evenly divisible by n. Your extracted array should be
sorted in ascending numerical order.

Examples:
If you ran extractEvenlyDivisible([1,2,3,4,5,6,7,8,9], 3) you would get a return value of [3,6,9].
If you ran extractEvenlyDivisible([1,9,3,4,3,6,7,8,9], 3) you would get a return value of [3,6,9].
"""

a = [1, 9, 3, 4, 3, 6, 7, 8, 9]


def extractEvenlyDivisible(array, divisor):
    b = set()

    def helper(arr):
        if(len(arr) == 0):
            return
        elif ((arr[0] % divisor) == 0):
            b.add(arr[0])
            arr.pop(0)
            return helper(arr)
        else:
            arr.pop(0)
            return helper(arr)
    helper(array)
    return sorted(b)


print(extractEvenlyDivisible(a, 3))
