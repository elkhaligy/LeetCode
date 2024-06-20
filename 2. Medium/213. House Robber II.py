def rob_db(nums: list[int]) -> int:

    def house_rob_i(nums: list[int]) -> int:

        dp_table = [0] * n
        dp_table[0] = nums[0]
        dp_table[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp_table[i] = max(nums[i] + dp_table[i - 2], dp_table[i - 1])
        return dp_table[-1]
    n = len(nums)
    if n == 1 or n == 2:
        return max(nums)
        
    return max(house_rob_i(nums[1:]), house_rob_i(nums[:-1]))

def rob_dp_in_place(nums: list[int]) -> int:
    n = len(nums)
    if n == 1 or n == 2:
        return max(nums)
    nums[1] = max(nums[0], nums[1])

    for i in range(2, n):
        nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
    return nums[-1]

print(rob_db(nums = [1,2,3]))
