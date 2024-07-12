def minKBitFlips(nums: list[int], k: int) -> int:
    n = len(nums)
    need_flipping = 0
    answer = 0
    flipped_index = [0] * n
    
    for i in range(n):
        if i >= k:
            need_flipping ^= flipped_index[i - k]
        if need_flipping == nums[i]:
            if i + k > n:
                return -1
            flipped_index[i] = 1
            need_flipping ^= 1
            answer += 1
    
    return answer


print(minKBitFlips())
