import heapq
def sortArray_priorityqueue(nums: list[int]) -> list[int]:
    heapq.heapify(nums) # o(n) operation
    ans = []
    while nums: # o(n)
        ans.append(heapq.heappop(nums)) # o(logn)
    # time complexity o(n logn)
    # space complecity o(n)
    return ans

def sortArray_bucketsort(nums: list[int]) -> list[int]:
    # Time complexity o(n)
    # Space complexity o(1) or o(100001)
    arr = [0] * 100001
    for num in nums:
        arr[num + 50000] += 1
    
    # for ind, num in enumerate(arr):
    #     if num > 0:
    #         print(f"Index = {ind}, Frequency = {num}")

    ans = []
    for ind, num in enumerate(arr):
        while num > 0:
            ans.append(ind - 50000)
            num -= 1
    
    return ans

print(sortArray_bucketsort(nums = [5,2,3,1]))
