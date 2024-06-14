def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    ans = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum > target: 
                right -= 1
            elif cur_sum < target:
                left += 1
            elif cur_sum == target:
                ans = cur_sum
                return ans
            if abs(target - cur_sum) < abs(target - ans):
                ans = cur_sum

    return ans

threeSumClosest(nums = [-1,2,1,-4], target = 1)