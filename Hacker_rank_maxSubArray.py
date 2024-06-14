# https://github.com/kilian-hu/hackerrank-solutions/tree/master/certificates/problem-solving-intermediate/maximum-subarray-value

def sumOfArray(nums):
    evenSum = 0
    oddSum = 0
    for i in range(0, len(nums), 2):
        evenSum += nums[i]
    for i in range(1, len(nums), 2):
        oddSum += nums[i]
    return (evenSum - oddSum) ** 2
        
def maxSubArray(nums):
    ans = float('-inf')
    for i in range(len(nums) - 1):
        for j in range(i , len(nums)):
            ans = max(ans, sumOfArray(nums[i:j+1]))
            print(nums[i:j+1])

    print(ans)
maxSubArray([1,-1,1,-1,1])