# number = left * left + right * right faster than number = left ** 2 + right ** 2
# right = int(c ** 0.5) faster than right = int(math.sqrt(c))

import math
def judgeSquareSum(c: int) -> bool:
    if c == 1 or c == 0:
        return True
    left = 0
    right = int(math.sqrt(c))

    while left != right:
        if left ** 2 + left ** 2 == c or right ** 2 + right ** 2 == c:
            return True
        if left ** 2 + right ** 2 > c:
            right -= 1
        elif left ** 2 + right ** 2 < c:
            left += 1
        else:
            return True
    return False

def judgeSquareSum_optimization(c: int) -> bool:
    if c == 1 or c == 0:
        return True
    left = 0
    right = int(math.sqrt(c))

    while left <= right:
        # number = left ** 2 + right ** 2
        number = left * left + right * right
        if number > c:
            right -= 1
        elif number < c:
            left += 1
        else:
            return True

    return False

print(judgeSquareSum_optimization(c = 1000000000000000))
