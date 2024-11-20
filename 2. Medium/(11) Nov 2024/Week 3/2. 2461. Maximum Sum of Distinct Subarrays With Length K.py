def maxSum(nums: list[int], k: int):
    left = right = 0
    answer = currSum = 0
    currentNumbers = set()

    while right < len(nums):
        currNumber = nums[right]
        if currNumber in currentNumbers:
            currentNumbers.remove(nums[left])
            currSum -= nums[left]
            left += 1
            continue
        currSum += currNumber
        currentNumbers.add(currNumber)

        if len(currentNumbers) == k:
            answer = max(answer, currSum)
            currentNumbers.remove(nums[left])
            currSum -= nums[left]
            left += 1

        right += 1

    return answer

print(maxSum(nums = [1,5,4,2,9,9,9], k = 3))