import heapq

def longestDiverseString(a: int, b: int, c: int) -> str:
    # Max heap (character count, charatcter)
    heap = []
    heapq.heappush(heap, (-a, 'a'))
    heapq.heappush(heap, (-b, 'b'))    
    heapq.heappush(heap, (-c, 'c'))

    result = []
    while heap:
        top_count, top_char = heapq.heappop(heap)
        top_count *= -1

        if len(result) >= 2 and result[-1] == result[-2] == top_char:
            if not heap:
                break
            second_top_count, second_top_char = heapq.heappop(heap)
            second_top_count *= -1
            result.append(second_top_char)
            second_top_count -= 1

            if second_top_count:
                heapq.heappush(heap, (-second_top_count, second_top_char))

            heapq.heappush(heap, (-top_count, top_char))
        else:
            result.append(top_char)
            top_count -= 1
            if top_count:
                heapq.heappush(heap, (-top_count, top_char))

    return ''.join(result)


print(longestDiverseString(a = 1, b = 1, c = 7))