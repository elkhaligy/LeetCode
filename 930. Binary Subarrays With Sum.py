from collections import defaultdict

def numSubarraysWithSum_prefixsum_freqdict(nums: list[int], goal: int) -> int:
    ans = 0
    prefixsum_lst = []
    
    prefixsum_lst.append(0)
    for num in nums:
        prefixsum_lst.append(num + prefixsum_lst[-1])
    
    frequency_dict = defaultdict(int)
    for num in prefixsum_lst:
        if num - goal in frequency_dict:
            ans += frequency_dict[num - goal]
            frequency_dict[num] += 1
        else:
            frequency_dict[num] += 1
            
    return ans

def numSubarraysWithSum_prefixsum_freqdict_combined(nums: list[int], goal: int) -> int:
    ans = 0
    total_sum = 0
    
    frequency_dict = defaultdict(int)
    frequency_dict[0] = 1
    for num in nums:
        total_sum += num
        if total_sum - goal in frequency_dict:
            ans += frequency_dict[total_sum - goal]
            frequency_dict[total_sum] += 1
        else:
            frequency_dict[total_sum] += 1
            
    return ans
print(numSubarraysWithSum_prefixsum_freqdict_combined(nums = [1,0,1,0,1], goal = 2))