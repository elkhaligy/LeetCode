import heapq, math
def pickGifts(gifts: list[int], k: int) -> int:
    gifts = [-1 * num for num in gifts]
    heapq.heapify(gifts)

    while k != 0:
        k -= 1
        maxElement = -1 * heapq.heappop(gifts)
        heapq.heappush(gifts, -1 * int(math.sqrt(maxElement)))



    return -1 * sum(gifts)


print(pickGifts(gifts = [54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,13,33,69,19,40,13,10,43,61,72], k = 7))
