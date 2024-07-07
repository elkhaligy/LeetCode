def numberOfAlternatingGroups(colors: list[int]) -> int:
    answer = 0 

    for i in range(len(colors)):
        if i + 1 and i + 2 < len(colors):
            if colors[i + 1] != colors[i + 2] and colors[i + 1] != colors[i]:
                answer += 1
        else:
            if i == len(colors) - 2:
                if colors[i + 1] != colors[0] and colors[i + 1] != colors[i]:
                    answer += 1
            else:
                if colors[0] != colors[1] and colors[0] != colors[i]:
                    answer += 1
    return answer

def numberOfAlternatingGroups_sliding_window(colors: list[int]) -> int:
    n = len(colors)
    left, right = 0, 2
    transitions, groups = 0, 0

    for i in range(1, 3):
        if colors[i] != colors[i - 1]:
            transitions += 1
    
    if transitions == 2:
        groups += 1
    
    while left < n - 1:
        if colors[left] != colors[(right - 1) % n]:
            transitions -= 1
        if colors[right % n] != colors[(right + 1) % n]:
            transitions += 1
        
        if transitions == 2:
            groups += 1
        right += 1
        left += 1
    return groups

def numberOfAlternatingGroups_sliding_window_2(colors: list[int]) -> int:
    n = len(colors)
    left, right = 0, 2
    transitions, groups = 0, 0

    for i in range(1, 3):
        if colors[i] != colors[i - 1]:
            transitions += 1
    
    if transitions == 2:
        groups += 1
    
    left += 1
    right += 1
    while left < n:
        if colors[left - 1] != colors[left]:
            transitions -= 1
        if colors[(right % n) - 1] != colors[(right) % n]:
            transitions += 1

        if transitions == 2:
            groups += 1
        right += 1
        left += 1
    return groups
print(numberOfAlternatingGroups_sliding_window_2(colors = [0,1,0,0,1]))
