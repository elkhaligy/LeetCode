def waysToSplitArray(nums: list[int]) -> int:
    # Input nums = [10, 4, -8, 7]
    # [10] [4, -8, 7] -> Valid
    # [10, 4] [-8, 7] -> Valid
    # [10, 4, -8] [7] -> Not Valid
    # Obtain the right sum and left sum array
    # Right sum array for example index 0 will contain the sum of all elements after it
    # index n - 1 will be 0 as there's no elements after it
    n = len(nums)
    if n == 2:
        return 1 if nums[0] > nums[1] else 0
    rightSum = [0] * n
    currSum = 0
    for i in range(n - 1, -1, -1):
        rightSum[i] = currSum
        currSum += nums[i]

    print(f"Right sum array = {rightSum}")

    # Obtain the left sum
    # left sum array for example at index 0 it will be 0 as there's no elements on the left
    leftSum = [0] * n
    currSum = 0
    for i in range(n):
        leftSum[i] = currSum
        currSum += nums[i]
    print(f"Left sum array = {leftSum}")

    # Now that you have both arrays you can loop from 0 to n - 2 inclusive and check if the left sum is larger than the right sum
    answer = 0
    for i in range(n - 1):
        if leftSum[i] + nums[i] >= rightSum[i]:
            answer += 1
    
    # This solution can be optimized further by using a one prefix sum array
    return answer
print(waysToSplitArray(nums = [0,0]))
