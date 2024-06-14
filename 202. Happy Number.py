from collections import defaultdict
def isHappy(n: int, repeated) -> bool:
    if n == 1:
        return True
    if repeated >= 2:
        return False
    s = str(n)
    result = 0
    for c in s:
        result += int(c) ** 2
    if result == n ** 2:
        repeated += 1
    
    return isHappy(result, repeated)

def isHappy_Sol2(n: int) -> bool:
    s = str(n)
    arr = []
    ans = 0
    while ans != 1:
        if s in arr:
            return False
        ans = 0
        for c in s:
            ans += int(c) ** 2
        arr.append(s)
        s = str(ans)

    return True if ans == 1 else False

# Best one
def isHappy_Sol3(n: int) -> bool:
    s = str(n)
    occu_dct = defaultdict(int)
    ans = 0
    while ans != 1:
        if occu_dct[s] > 1:
            return False
        ans = 0
        for c in s:
            ans += int(c) ** 2
        occu_dct[s] += 1
        s = str(ans)

    return True if ans == 1 else False

print(isHappy_Sol3(19))