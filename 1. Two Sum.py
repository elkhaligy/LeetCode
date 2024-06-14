def twoSum_bruteforce(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if target - nums[j] == nums[i]:
                return [i,j]

def twoSum_hashmap_twopass(nums: list[int], target: int) -> list[int]:
    comp_dct = {}

    for index, item in enumerate(nums):
        comp_dct[target - item] = index
        
    for index, item in enumerate(nums):
        if item in comp_dct and index != comp_dct[item]:
            return [index, comp_dct[item]]
        
def twoSum_hashmap_onepass(nums: list[int], target: int) -> list[int]:
    dct = {}
    
    for index, item in enumerate(nums):
        if item in dct:
            return [index, dct[item]]
        else:
            dct[target - item] = index
 

print(twoSum_hashmap_onepass( nums = [3,2,4], target = 6))