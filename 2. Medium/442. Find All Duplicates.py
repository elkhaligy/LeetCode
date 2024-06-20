def findDuplicates_hashmap_oN(nums: list[int]) -> list[int]:
    hash_table = {}

    for item in nums:
        if item not in hash_table:
            hash_table[item] = 1
        else:
            hash_table[item] += 1

    return [key for key, value in hash_table.items() if value == 2]

def findDuplicates_numsAsIndices(nums: list[int]) -> list[int]:
    ans = []
    for item in nums:
        if nums[abs(item) - 1] < 0:
            ans.append(abs(item))
        else:
            nums[abs(item) - 1] *= -1
    
    return ans

print(findDuplicates_numsAsIndices([4,3,2,7,8,2,3,1]))