from collections import Counter
def singleNumber(nums: list[int]) -> int:
    dct = Counter(nums)
    for key, val in dct.items():
        if val == 1:
            return key
        

def singleNumber2(nums: list[int]) -> int:
    ans = 0
    for num in nums:
        ans = ans ^ num
    return ans
print(singleNumber2([4,1,2,1,2]))