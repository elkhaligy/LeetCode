def jump(nums: list[int]) -> int:
    jump_cnt = nums[0]
    min_jumps = 0
    for cur_jump in nums:
        if jump_cnt < 0:
            min_jumps = -1
            break
        if cur_jump > jump_cnt:
            jump_cnt = cur_jump
        jump_cnt -= 1
        min_jumps += 1

    return min_jumps



jump(nums = [2,3,1,1,4])