from collections import Counter, defaultdict

def subarraySum_prefixsum_notworking(nums: list[int], k: int) -> int:
    # The problem with this approach is if a sum is repeated more than 1
    # The answer is increased by only 1, so we need frequency dictionary
    # nums = [1,1,1,0,1,1], k = 2
    # [0, 1, 2, 3, 3, 4, 5] as you see 5 - 2 is 3 but 3 is there 2 times so
    # 2 subarrays can be constructed yet this loop adds only 1
    ans = 0
    prefixsum_lst = []

    prefixsum_lst.append(0)
    for num in nums:
        prefixsum_lst.append(num + prefixsum_lst[-1])
    

    for i in range(len(prefixsum_lst) - 1, -1, -1):
        if (prefixsum_lst[i] - k) in prefixsum_lst:
            ans += 1
    print(prefixsum_lst)
    print(ans)

def subarraySum_prefixsum_frequencyDic(nums: list[int], k: int) -> int:
    ans = 0
    prefixsum_lst = []

    prefixsum_lst.append(0)
    for num in nums:
        prefixsum_lst.append(num + prefixsum_lst[-1])
    
    freq_dic = Counter(prefixsum_lst)
    for i in range(len(prefixsum_lst) - 1, -1, -1):
        if (prefixsum_lst[i] - k) in freq_dic:
            ans += freq_dic[prefixsum_lst[i] - k]
    print(prefixsum_lst)
    print(ans)

def subarraySum_prefixsum_combined(nums: list[int], k: int) -> int:
    # This solution gets rid of the prefixsum list and combine it with the dictionary
    # on one pass
    ans = 0
    _sum = 0
    # prefix dct: key -> prefix sum, value -> frequency
    prefix_dct = defaultdict(int)
    prefix_dct[0] = 1

    for num in nums:
        _sum += num
        ans += prefix_dct[_sum - k]
        prefix_dct[_sum] += 1
        
    return ans

print(subarraySum_prefixsum_frequencyDic(nums = [1,1,1,0,1,1], k = 2))