def minDifference_sol1(nums: list[int]) -> int:
    n = len(nums)
    if n <= 4:
        return 0
    
    nums.sort()
    # Remove largest three elements
    answer1 = max(nums[0:-3]) - min(nums[0:-3])
    # Remove smallest three elements
    answer2 =  max(nums[3:]) - min(nums[3:])
    # Remove 1 small 2 large
    answer3 = max(nums[1:-2]) - min(nums[1:-2])
    # Remove 1 large 2 small
    answer4 = max(nums[2:-1]) - min(nums[2:-1])
    return min(answer1, answer2, answer3, answer4)

def minDifference_sol2(nums: list[int]) -> int:
    n = len(nums)
    if n <= 4:
        return 0
    
    nums.sort()
    
    answer = float('inf')
    for i in range(4):
        end = n + i - 4
        answer = min(answer, nums[end] - nums[i])
    
    return answer


print(minDifference_sol2(nums = [6,6,0,1,1,4,6]))
