from collections import defaultdict, Counter

def subarraysDivByK_prefixsum_frequencyDic(nums: list[int], k: int) -> int:
    # This is just like 1, but we don't need to take care of subarray length
    # we also want to take care of frequency as we want total number of subarrays
    ans = 0
    prefixsum_mod_lst = []

    prefixsum_mod_lst.append(0)
    for num in nums:
        prefixsum_mod_lst.append((num + prefixsum_mod_lst[-1]) % k)
    print(prefixsum_mod_lst)
    prefix_mod_dct = defaultdict(int)
    
    for num in prefixsum_mod_lst:
        if num in prefix_mod_dct:
            ans += prefix_mod_dct[num]
            prefix_mod_dct[num] += 1
        else:
            prefix_mod_dct[num] += 1
            
    return ans
def subarraysDivByK_prefixsum_frequencyDic_refactored(nums: list[int], k: int) -> int:
    prefix_mod_sum = 0
    prefix_mod_sum_counts = Counter()
    prefix_mod_sum_counts[0] = 1

    ans = 0
    for num in nums:
        prefix_mod_sum = (prefix_mod_sum + num) % k
        ans += prefix_mod_sum_counts[prefix_mod_sum]
        prefix_mod_sum_counts[prefix_mod_sum] += 1
        
    return ans
        

def subarraysDivByK(nums: list[int], k: int) -> int:
    ans = 0
    # prefix mod dct: key -> prefix mod sum, value -> frequency
    prefix_mod_dct = defaultdict(int)
    prefix_mod_dct[0] = 1
    mod_sum = 0
    for num in nums:
        mod_sum = (mod_sum + num) % k
        ans += prefix_mod_dct[mod_sum]
        prefix_mod_dct[mod_sum] += 1
        
    return ans

print(subarraysDivByK_prefixsum_frequencyDic_refactored(nums = [4,5,0,-2,-3,1], k = 5))