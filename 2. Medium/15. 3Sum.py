from collections import defaultdict
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = set()
    res = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum == 0:
                cur_list = [nums[i], nums[left], nums[right]]
                if cur_list not in res:
                    res.append(cur_list[:])
                left += 1
                right -= 1
            elif cur_sum > 0: 
                right -= 1
            elif cur_sum < 0:
                left += 1
    return res
def threeSum_Sol2(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(0, len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        if i != 0 and nums[i] == nums[i-1]:
            continue
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and l < r:
                    l += 1
            elif cur_sum > 0:
                right -= 1
            else:
                left += 1


    return result


print(threeSum_Sol2(nums = [-1,0,1,2,-1,-4]))