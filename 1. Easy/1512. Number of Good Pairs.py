from collections import Counter
import math
def numIdenticalPairs(nums: list[int]) -> int:
    occu_dct = Counter(nums)
    ans = 0
    for value in occu_dct.values():
        if value > 1:
             ans += math.factorial(value) // (2 * math.factorial((value-2)))

    return ans 
def numIdenticalPairs_Sol2(nums: list[int]) -> int:
    occu_dct = Counter(nums)
    return sum([math.comb(item, 2) for item in occu_dct.values()])

print(numIdenticalPairs(nums = [1,2,3]))