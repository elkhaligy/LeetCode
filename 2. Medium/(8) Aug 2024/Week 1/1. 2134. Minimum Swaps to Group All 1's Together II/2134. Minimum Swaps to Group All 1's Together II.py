def minSwaps(nums: list[int]) -> int:
    # Prepare the initial window
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    if 1 not in freq_dict:
        return 0
    window_size = freq_dict[1]
    initial_ones = 0
    for i in range(window_size):
        if nums[i] == 1:
            initial_ones += 1
    
    # Start sliding the windooow
    left = 0
    right = window_size - 1
    n = len(nums)
    current_ones = initial_ones
    ans = float('inf')

    while left < n:
        ans = min(ans, window_size - current_ones)
        if nums[left] == 1:
            current_ones -= 1
        if nums[(right + 1) % n] == 1:
            current_ones += 1
        left += 1
        right += 1
    
    return ans



print(minSwaps(nums = [1,1]))