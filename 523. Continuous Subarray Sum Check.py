from collections import defaultdict

def checkSubarraySum_bruteforce94o99(nums: list[int], k: int) -> bool:
    n = len(nums)
    cur_sum = 0
    for i in range(n):
        cur_sum = nums[i]
        for j in range(i + 1, n):
            cur_sum += nums[j]
            if cur_sum % k == 0:
                return True
    
    return False

def checkSubarraySum_failedtry(nums: list[int], k: int) -> bool:
    if len(nums) == 1:
        return nums[0] % k
    dct = {}
    cur_sum = 0
    arr = []
    for i in range(len(nums)):
        cur_sum += nums[i]
        arr.append(cur_sum % k)
    
    print(arr)

    for i, num in enumerate(arr):
        if num in dct:
            dct[num].append(i)
        else:
            dct[num] = []
            dct[num].append(i)

    print(dct)
    for key, value in dct.items():
        if key == 0:
            if len(value) > 1:
                for i in range(len(value) - 1):
                    if value[i + 1] - value[i] == 1:
                        return True
        elif len(value) == 1:
            continue
        else:
            for i in range(len(value)):
                for j in range(i + 1, len(value)):
                    if len(nums[value[i] + 1:value[j]]) < 2:
                        continue
                    if sum(nums[value[i] + 1:value[j]]) % k == 0:
                        return True
                
    # print(dct)
    return False

def checkSubarraySum_prefixsum(nums: list[int], k: int) -> bool:
    n = len(nums)
    print(f"Original list: {nums}")

        
    # prefix sum list contains the total sum on the left of an element
    # example:
    # nums = [23,2,4,6,7], k = 6
    # prefix_sums = [0, 23, 25, 29, 35, 42]
    # so it is always with a lentgth more than the original list by one
    # if you want to have the sum of a subarray starting from i = 1 and ending at j = 4 inclusive
    # which is [2, 4, 6, 7]
    # then you can find that from the prefix_sums 
    # prefix_sums[j + 1] - prefix_sums[i] = 42 - 23 = 19
    prefix_sum_lst = []
    prefix_sum_lst.append(0)
    for num in nums: 
        prefix_sum_lst.append(num + prefix_sum_lst[-1])
    print(f"Prefix Sum list: {prefix_sum_lst}")
    
    # Prefix mod lst
    # it is an extension to the prefix sum lst
    # when you want to find a subarray that has the sum that is divisible by k
    # then if this subarray starts at i and ends at j, we can find it's sum using the prefix sum lst
    # prefix_sums[j + 1] - prefix_sums[i] = sum
    # so if sum % k == 0 then we found a subarray that achieves what is needed
    # use the mathematical relation
    # (prefix[j + 1] - prefix[i]) % k = 0
    # prefix[j + 1] % k = prefix[i] % k
    # So if we have a subarray i to j and we found that value at index j + 1 same as value at index i
    # we are sure that this subarray achieves what is needed
    prefix_mod_arr = []
    for num in prefix_sum_lst:
        prefix_mod_arr.append(num % k )

    print(f"Prefix Mod list: {prefix_mod_arr}")

    # So easily, if you found the same number in prefix mod list and these two numbers
    # has indices difference of 2 or more then you have a subarray that achieves this case of its sum % k == 0
    my_dct = {}
    for i, num in enumerate(prefix_mod_arr):
        if num in my_dct:
            my_dct[num].append(i)
        else:
            my_dct[num] = []
            my_dct[num].append(i)
    for value in my_dct.values():
        if value[-1] - value[0] > 1:
            return True
    return False


def checkSubarraySum_prefixsum_opt(nums: list[int], k: int) -> bool:
    prefix_sum_lst = []
    prefix_sum_lst.append(0)
    for num in nums: 
        prefix_sum_lst.append(num + prefix_sum_lst[-1])
        
    prefix_mod_dct = defaultdict(int)
    
    for i, num in enumerate(prefix_sum_lst):
        cur_mod = num % k
        if cur_mod in prefix_mod_dct:
            if i - prefix_mod_dct[cur_mod] > 1:
                return True
        else:
            prefix_mod_dct[cur_mod] = i 
    
    return False

print(checkSubarraySum_prefixsum( nums = [23,2,4,6,7], k = 6))