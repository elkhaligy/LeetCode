def canJump(nums: list[int]) -> bool:
    max_index = 0
    for i, num in enumerate(nums):
        if i > max_index:
            return False
        max_index = max(max_index, num + i)

    return True

def canJump_sol2(nums: list[int]) -> bool:
    jump_cnt = nums[0]

    for cur_jump in nums:
        if jump_cnt < 0:
            return False
        if cur_jump > jump_cnt:
            jump_cnt = cur_jump
        jump_cnt -= 1
    return True
print(canJump_sol2(nums = [2,3,1,0,4]))