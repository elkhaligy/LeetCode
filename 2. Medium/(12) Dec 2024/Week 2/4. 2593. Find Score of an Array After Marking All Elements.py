import heapq

def findScore_TLE(nums: list[int]) -> int:
    # Brute force
    n = len(nums)
    marked = [0] * n
    score = 0

    while sum(marked) != n:
        curMin = float('inf')
        curMinIndex = 0
        for i in range(n):
            if nums[i] < curMin and marked[i] == 0:
                curMin = nums[i]
                curMinIndex = i
        score += curMin
        marked[curMinIndex] = 1
        if curMinIndex < n - 1:
            marked[curMinIndex + 1] = 1
        if curMinIndex > 0:
            marked[curMinIndex - 1] = 1

    return score

def findScore(nums: list[int]) -> int:
    # Heap
    n = len(nums)
    marked = [0] * n
    markedSum = 0
    score = 0
    numsIndex = [(num, index) for index, num in enumerate(nums)]
    heapq.heapify(numsIndex)
    # print(numsIndex)

    while markedSum != n:
        minVal, index = heapq.heappop(numsIndex)
        if marked[index] == 0:
            score += minVal
            marked[index] = 1
            markedSum += 1
            if index < n - 1 and marked[index + 1] == 0:
                marked[index + 1] = 1
                markedSum += 1
            if index > 0  and marked[index - 1] == 0:
                marked[index - 1] = 1
                markedSum += 1
    
    return score
        
    

print(findScore(nums = [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]))
