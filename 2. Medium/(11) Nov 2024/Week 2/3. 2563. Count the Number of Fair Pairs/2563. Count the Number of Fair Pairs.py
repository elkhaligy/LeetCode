def countFairPairs_bruteforce(nums: list[int], lower: int, upper: int) -> int:
    n = len(nums)
    fair_pair_counter = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            curr_sum = nums[i] + nums[j]
            if curr_sum >= lower and curr_sum <= upper:
                fair_pair_counter += 1


    return fair_pair_counter

def binary_search(nums: list[int], low, high, target):
    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
        
        
    return low
def countFairPairs_bs(nums: list[int], lower: int, upper: int) -> int:
    n = len(nums)
    nums.sort()
    fair_pair_counter = 0
    high_index = low_index = 0

    for i in range(n):
        
        low_index = binary_search(nums = nums, 
                                  low = i + 1, 
                                  high = n - 1, 
                                  target = lower - nums[i]) 

        high_index = binary_search(nums = nums, 
                                  low = i + 1, 
                                  high = n - 1, 
                                  target = upper - nums[i] + 1) # The +1 here indicates that I need the index of the first element larger than 6, it will not be included in the window 

        fair_pair_counter += high_index - low_index

    return fair_pair_counter
print(countFairPairs_bs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
