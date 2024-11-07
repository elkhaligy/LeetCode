from heapq import heappush
from heapq import heappop
def maxScore_TLE(nums1: list[int], nums2: list[int], k: int) -> int:
    pairs = list(zip(nums1, nums2))
    pairs.sort(key=lambda a: a[1], reverse=True)
    ans = 0
    sum_list = []
    for a, b in pairs:
        sum_list.append(a)
        if len(sum_list) > k:
            sum_list.remove(min(sum_list))
        if len(sum_list) == k:
            cur_sum = sum(sum_list)
            ans = max(ans, cur_sum * b)

        

    return ans

def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    pairs = list(zip(nums1, nums2))
    pairs.sort(key=lambda a: a[1], reverse=True)
    ans = 0
    sum_heap = []
    cur_sum = 0
    for a, b in pairs:
        heappush(sum_heap, a)
        cur_sum += a
        if len(sum_heap) > k:
            cur_sum -= heappop(sum_heap)
        if len(sum_heap) == k:
            ans = max(ans, cur_sum * b)

        

    return ans
print(maxScore(nums1 = [2,1,14,12], nums2 = [11,7,13,6], k = 3))
