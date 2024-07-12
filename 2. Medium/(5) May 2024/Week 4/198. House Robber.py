def rob_db(nums: list[int]) -> int:
    n = len(nums)
    if n == 1 or n == 2:
        return max(nums)
    
    dp_table = [0] * n
    dp_table[0] = nums[0]
    dp_table[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp_table[i] = max(nums[i] + dp_table[i - 2], dp_table[i - 1])
    return dp_table[-1]

def rob_dp_in_place(nums: list[int]) -> int:
    n = len(nums)
    if n == 1 or n == 2:
        return max(nums)
    nums[1] = max(nums[0], nums[1])

    for i in range(2, n):
        nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
    return nums[-1]

def rob_recursive(nums: list[int]) -> int:
    n = len(nums)

    def rec(index: int):
        if index < 0:
            return 0
        if index == 0:
            return nums[0]
        pick = nums[index] + rec(index - 2)
        no_pick = rec(index - 1)
        ans = max(pick, no_pick)
        return ans

    return rec(n - 1)

def rob_recursive_memoization(nums: list[int]) -> int:
    n = len(nums)
    dp_dict = {}

    def rec(index: int):
        if index < 0:
            return 0
        elif index == 0:
            return nums[0]
        elif index in dp_dict:
            return dp_dict[index]
        pick = nums[index] + rec(index - 2)
        no_pick = rec(index - 1)
        ans = max(pick, no_pick)
        dp_dict[index] = ans
        return ans

    return rec(n - 1)

print(rob_recursive_memoization(nums = [2,1,1,2]))
        