def minimumSubarrayLength(nums: list[int], k: int) -> int:
    # Solution is dynamic sliding window
    left = right = 0
    n = len(nums)
    window_bits = [0] * 32
    min_len = float('inf')

    while right < n:
        # Add current number to the window
        for pos in range(32):
            if nums[right] & (1 << pos):
                window_bits[pos] += 1

        # Get the total result of that window
        curr_total = 0
        for pos in range(32):
            if window_bits[pos]:
                curr_total |= 1 << pos
        
        # If the current total is >= k shrink the window
        while left <= right and  curr_total >= k:
            min_len = min(min_len, right - left + 1)
            for pos in range(32):
                if nums[left] & (1 << pos):
                    window_bits[pos] -= 1
                    
            curr_total = 0
            for pos in range(32):
                if window_bits[pos]:
                    curr_total |= 1 << pos
            left += 1
        
        right += 1
    
    return -1 if min_len == float('inf') else min_len


print(minimumSubarrayLength(nums = [2,1,8], k = 10))