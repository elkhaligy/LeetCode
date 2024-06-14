from collections import Counter
def majorityElement(nums: list[int]) -> int:
    n = len(nums)
    occu_dct = Counter(nums)
    maj = n // 2
    for key, value in occu_dct.items():
        if value > maj:
            return key

def faa(num):
    return num*num
def majorityElementSol2(nums: list[int]) -> int:
    occu_dct = Counter(nums)
    return max(occu_dct.keys(), key=occu_dct.get)
print(majorityElementSol2(nums = [3,5,2,3]))