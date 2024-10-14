import heapq, math

def maxKelements(nums: list[int], k: int) -> int:
    heap = []
    ans = 0

    # Populate max heap
    for num in nums:
        heapq.heappush(heap, -1 * num)
    
    while k > 0:
        max_element = -1 * heapq.heappop(heap)
        ans += max_element
        heapq.heappush(heap, -1 * math.ceil(max_element / 3))
        k -= 1

    return ans

print(maxKelements(nums = [10,10,10,10,10], k = 5))