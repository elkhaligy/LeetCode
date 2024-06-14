def appendCharacters_bruteforce(s: str, t: str) -> int:
    ans = 0
    flag = False
    for ind, chr in enumerate(t):
        
        if s.find(chr) == -1:
            ans = ind
            flag = True
            break
        else:
            s = s[s.find(chr) + 1:]

    if ans == 0 and flag == True:
        return len(t) - ans
    elif ans != 0:
        return len(t) - ans
    else:
        return 0
    
def appendCharacters(s: str, t: str) -> int:
    t_ptr = 0
    s_ptr = 0

    while t_ptr < len(t) and s_ptr < len(s):

        if s[s_ptr] != t[t_ptr]:
            s_ptr += 1
        elif s[s_ptr] == t[t_ptr]:
            s_ptr += 1
            t_ptr += 1
    
    if t_ptr == len(t):
        return 0
    else:
        return len(t) - t_ptr
    print(t_ptr)
    
print(appendCharacters(s = "z", t = "zaq"))
