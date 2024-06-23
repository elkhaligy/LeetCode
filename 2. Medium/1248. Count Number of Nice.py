def numberOfSubarrays(nums: list[int], k: int) -> int:
    cur_sum = 0
    ans = 0
    # key -> prefix sum, value -> its frequency
    prefix_dct = {}

    prefix_dct[cur_sum] = 1
    for i in range(len(nums)):
        cur_sum += nums[i] % 2
        if cur_sum - k in prefix_dct:
            ans += prefix_dct[cur_sum - k]
        prefix_dct[cur_sum] = prefix_dct.get(cur_sum, 0) + 1

    return ans

print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
