def countSegments(s: str) -> int:
    # that's it lol
    return len(s.split())

def countSegments_no_cheating_sol(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    
    ans = 1
    space_flag = False

    for c in s:
        if c != ' ' and space_flag == True:
            ans += 1
            space_flag = False
        elif c == ' ':
            space_flag = True

    return ans