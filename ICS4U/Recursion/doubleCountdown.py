"""
def doubleCountdown(value):
  for x in range(value, 0, -1):
    print(x)
  for x in range(value, 0, -1):
    print(x-1)

doubleCountdown(5)

"""


def recursiveCountdown(value):
    def helper(n, val):
        if n <= 0 and val == 1:
            print(0)
            return
        if n == 0 and val == 0:
            return helper(value - 1, 1)
        print(n)
        return helper(n - 1, val)
    helper(value, 0)


recursiveCountdown(6)
