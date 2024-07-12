from collections import Counter
def majorityElement(nums: list[int]) -> int:
    n = len(nums)
    occu_dct = Counter(nums)
    maj = n // 2
    for key, value in occu_dct.items():
        if value > maj:
            return key

def majorityElementSol2(nums: list[int]) -> int:
    occu_dct = Counter(nums)
    return max(occu_dct.keys(), key=occu_dct.get)

def majorityElement_sol3(nums: list[int]) -> int:
    # moore
    candidate = nums[0]
    candidate_count = 1
    for num in nums[1:]:
        if num != candidate:
            candidate_count -= 1
            if candidate_count == 0:
                candidate = num
                candidate_count += 1
        else:
            candidate_count += 1
    
    return candidate
print(majorityElementSol2(nums = [3,5,2,3]))