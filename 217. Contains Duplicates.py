# https://leetcode.com/problems/contains-duplicate/description/
from collections import defaultdict
def containsDuplicate_BruteForce(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False

def containsDuplicate_Sorting(nums):
    nums.sort()
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

def containsDuplicate_HashMap(nums):
    # Using dictionary
    hashTable = {}
    for i in range(0,len(nums)):
        if nums[i] in hashTable:
            return True
        else:
            hashTable[nums[i]] = i
    return False

def containsDuplicate_Set(nums):
    # Using set
    hashTable = set()
    for i in range(0,len(nums)):
        if nums[i] in hashTable:
            return True
        else:
            hashTable.add(nums[i])
    return False

def containsDuplicate_Unique(nums):
    nums.sort()
    mySet = set(nums)

    if len(nums) == len(mySet):
        return False
    return True

def containsDuplicate_DefaultDect(nums):
    dct = defaultdict(int)
    for num in nums:
        if num in dct:
            return True
        else:
            dct[num] = num
    return False
print(containsDuplicate_DefaultDect([1,2,3,1]))