def minDays_bruteforce(bloomDay: list[int], m: int, k: int) -> int:
    n = len(bloomDay)
    if m * k > n:
        return -1
    
    sorted_bloomDay = sorted(bloomDay)
    sorted_unq_bloomDay = []
    temp_set = set()

    for day in sorted_bloomDay:
        if day not in temp_set:
            sorted_unq_bloomDay.append(day)
        temp_set.add(day)

    answer = float('inf')

    for day in sorted_unq_bloomDay:
        bouq_num = get_bouq_num(bloomDay, day, k)

        if bouq_num >= m:
            answer = min(answer, day)

    return -1 if answer == float('inf') else answer

def get_bouq_num(bloomDay: list[int], mid: int, k: int) -> int:
    conseq_flowers = 0
    bouq_num = 0

    for day in bloomDay:
        if day <= mid:
            conseq_flowers += 1
        else:
            conseq_flowers = 0
        if conseq_flowers == k:
            bouq_num += 1
            conseq_flowers = 0

    return bouq_num

def minDays_binarysearch(bloomDay: list[int], m: int, k: int) -> int:
    n = len(bloomDay)

    if m * k > n:
        return -1
    
    left = min(bloomDay)
    right = max(bloomDay)
    answer = float('inf')

    while left <= right:
        mid = left + (right - left) // 2

        bouq_num = get_bouq_num(bloomDay, mid, k)
        if bouq_num >= m:
            right = mid - 1
            answer = min(answer, mid)
        elif bouq_num < m:
            left = mid + 1

    return answer
print(minDays_bruteforce(bloomDay =[7,7,7,7,12,7,7], m = 2, k = 3))