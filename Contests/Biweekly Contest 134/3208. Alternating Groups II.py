def numberOfAlternatingGroups_sliding_window_1(colors: list[int], k: int) -> int:
    n = len(colors)
    groups = 0
    
    if k > n:
        return 0
    
    curr_trans = 0
    for i in range(k - 1):
        if colors[i % n] != colors[(i + 1) % n]:
            curr_trans += 1
    
    if curr_trans == k - 1:
        groups += 1
    
    for start in range(1, n):
        left = (start - 1) % n
        right = (start + k - 2) % n

        if colors[left] != colors[start % n]:
            curr_trans -= 1
        if colors[right] != colors[(start + k - 1) % n]:
            curr_trans += 1
        
        if curr_trans == k - 1:
            groups += 1
    
    return groups

def numberOfAlternatingGroups_sliding_window_2(colors: list[int], k: int) -> int:
    n = len(colors)
    left, right = 0, k - 1
    transitions, groups = 0, 0

    for i in range(1, k):
        if colors[i] != colors[i - 1]:
            transitions += 1
    
    if transitions == k - 1:
        groups += 1
    
    left += 1
    right += 1

    while left < n:
        if colors[left - 1] != colors[left]:
            transitions -= 1
        if colors[(right % n) - 1] != colors[(right) % n]:
            transitions += 1
        if transitions == k - 1:
            groups += 1
        left += 1
        right += 1
    return groups
    # for start in range(1, n):
    #     left = (start - 1) % n
    #     right = (start + k - 2) % n

    #     if colors[left] != colors[start % n]:
    #         curr_trans -= 1
    #     if colors[right] != colors[(start + k - 1) % n]:
    #         curr_trans += 1
        
    #     if curr_trans == k - 1:
    #         groups += 1
    
    # return groups

print(numberOfAlternatingGroups_sliding_window_2(colors = [0,1,0,0,1,0,1], k = 6))
