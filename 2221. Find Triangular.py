def triangularSum_recursive(nums: list[int]) -> int:
    
    def recursion(nums: list[int]):
        if len(nums) == 1:
            return nums[0]

        new_nums = []
        for ind in range(0, len(nums) - 1, 1):
            new_nums.append((nums[ind] + nums[ind + 1]) % 10)

        
        return recursion(new_nums)
    
    return recursion(nums)


print(triangularSum_recursive(nums = [1,2,3,4,5]))