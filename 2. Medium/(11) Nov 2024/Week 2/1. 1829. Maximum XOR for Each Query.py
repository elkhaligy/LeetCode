def getMaximumXor(nums: list[int], maximumBit: int) -> list[int]:
    n = len(nums)
    prefix_xor = [0] * n
    prefix_xor[0] = nums[0]
    for i in range(1, n):
        prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]

    ans = [0] * len(nums)

    mask = 2 ** maximumBit - 1

    for i in range(n):
        current_xor = prefix_xor[n - 1 - i]
        ans[i] = current_xor ^ mask

    return ans

getMaximumXor(nums = [0,1,1,3], maximumBit = 2)