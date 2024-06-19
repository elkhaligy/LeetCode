def minDays_bruteforce(bloomDay: list[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1
    
    temp_lst = sorted(bloomDay)
    temp_lst2 = []
    temp_set = set()
    for day in temp_lst:
        if day not in temp_set:
            temp_lst2.append(day)
        temp_set.add(day)

    #print(temp_lst2) 
    bouq_count = 0
    cons = 0
    for day in temp_lst2:
        cons = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] == day:
                bloomDay[i] = 'X'
        for i in range(len(bloomDay)):
            if bloomDay[i] == 'X':
                cons += 1
            else:
                cons = 0
            if cons == k:
                bouq_count += 1
                cons = 0
        if bouq_count >= m:
            return day
        else:
            bouq_count = 0
    
    return -1


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
print(minDays_binarysearch(bloomDay =[7,7,7,7,12,7,7], m = 2, k = 3))