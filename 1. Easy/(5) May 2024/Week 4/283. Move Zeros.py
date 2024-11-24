def moveZeroes(nums: list[int]) -> None:
    ans = []
    zeros_cnt = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros_cnt += 1
        else:
            ans.append(nums[i])
    
    for i in range(zeros_cnt):
        ans.append(0)
    
    return ans

def moveZeroes_inplace(nums: list[int]) -> None:
    if len(nums) <= 1:
        return nums

    start = 0
    next = 1

    while next != len(nums):
        if nums[start] == 0 and nums[next] != 0:
            nums[start], nums[next] = nums[next], nums[start]
            start += 1
            next += 1
        elif nums[start] == 0 and nums[next] == 0:
            next += 1
        else:
            start += 1
            next += 1
    
    print(nums)

    pass


def moveZeroes_inplace_2(nums: list[int]) -> None:
    if len(nums) <= 1:
        return nums

    start = 0
    end = 1

    while end < len(nums):
        if nums[start] == 0 and nums[end] != 0:
            nums[end], nums[start] = nums[start], nums[end]
            start += 1
            end += 1
        elif nums[start] == 0 and nums[end] == 0:
            end += 1
        else:
            start += 1
            end += 1

    return nums

print(moveZeroes_inplace_2(nums = [0,1,0,3,12]))
