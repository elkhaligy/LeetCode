def longestCommonPrefix_bruteforce(strs: list[str]) -> str:
    ans = []
    flag = False
    min_len_str = min(strs, key=len)

    for j in range(len(min_len_str)):
        cur = strs[0][j]
        for i in range(1, len(strs)):
            if strs[i][j] != cur:
                flag = True
                break
        if flag == True:
            break
        else:
            ans.append(cur)

    return ''.join(ans)

def longestCommonPrefix_optimized(strs: list[str]) -> str:
    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_len = min(len(first), len(last))
    ans = []

    for i in range(min_len):
        if first[i] == last[i]:
            ans.append(first[i])
        else:
            break
    
    return ''.join(ans)


print(longestCommonPrefix_optimized(["flower","flow","flight"]))