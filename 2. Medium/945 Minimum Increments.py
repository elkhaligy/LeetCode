from collections import Counter
def minIncrementForUnique_bruteforce(nums: list[int]) -> int:
    unique_nums = set(nums)
    nums_frequencies = Counter(nums)
    min_steps = 0
    prev_min_steps = 0
    
    for number, frequency in nums_frequencies.items():
        while frequency > 1:
            while number in unique_nums:
                number += 1
                min_steps += 1
                min_steps += prev_min_steps
            unique_nums.add(number)
            frequency -= 1
            prev_min_steps = min_steps
        prev_min_steps = 0
    
    return min_steps
    
def minIncrementForUnique_greedy(nums: list[int]) -> int:
    nums.sort()
    prev_value = nums[0]
    min_steps = 0
    
    for ind in range(1, len(nums)):
        if nums[ind] == prev_value or nums[ind] < prev_value:
            tmp = nums[ind]
            nums[ind] = prev_value + 1
            min_steps += nums[ind] - tmp 
        prev_value = nums[ind]
    return min_steps        

print(minIncrementForUnique_greedy(nums = [3,2,1,2,1,7]))
