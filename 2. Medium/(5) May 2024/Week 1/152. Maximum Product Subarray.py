def maxProduct_bruteforce(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    prod = 1
    ans = float('-inf')

    for i in range(len(nums)):
        for j in range(i,len(nums)):
            prod *= nums[j]
            ans = max(ans,prod)
        prod = 1

    return ans


def maxProduct_optimized(nums: list[int]) -> int:
    leftProd = 1
    rightProd = 1
    ans = nums[0]

    for i in range(len(nums)):
        if leftProd == 0:
            leftProd = 1
        if rightProd == 0:
            rightProd = 1
        leftProd *= nums[i]
        rightProd *= nums[len(nums)-1-i]
        ans = max(ans,leftProd,rightProd)

    return ans

print(maxProduct_optimized(nums = [2,3,-2,4]))