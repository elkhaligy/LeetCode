def findDuplicate(nums: list[int]) -> int:
    lst = [1] * len(nums)

    for num in nums:
        if lst[num - 1] == -1:
            return num
        else:
            lst[num - 1] = -1



print(findDuplicate(nums = [1,3,4,2,2]))