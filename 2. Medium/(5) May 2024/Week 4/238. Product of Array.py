def productExceptSelf_Bruteforce(nums: list[int]) -> list[int]:
    ans = []
    prod = 1
    r = 0
    while r<len(nums):
        for i in range(r+1,len(nums)):
            prod *= nums[i]
        for i in range(0,r):
            prod *=nums[i]
        r += 1
        ans.append(prod)
        prod = 1
    return ans

def productExceptSelf_oN(nums: list[int]) -> list[int]:
    n = len(nums)
    left_product = [0] * n
    right_product = [0] * n

    print(right_product)

    cur_product = 1
    left_product[0] = 1

    for i in range(1, n):
        cur_product *= nums[i - 1]
        left_product[i] = cur_product

    cur_product = 1
    right_product[-1] = 1

    for i in range(n - 2, -1, -1):
        cur_product *= nums[i + 1]
        right_product[i] = cur_product
    
    for i in range(n):
        left_product[i] *= right_product[i]

    return left_product

def productExceptSelf_oN_OneList(nums: list[int]) -> list[int]:
    out = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        out[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        out[i] *= postfix
        postfix *= nums[i]
    return out

print(productExceptSelf_oN_OneList(nums = [1,2,3,4]))