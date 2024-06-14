def sol_1(arr: list[str]):
    arr.sort()

    first = arr[0]
    last = arr[-1]
    min_len = min(len(first), len(last))
    ans = []
    for i in range(min_len):
        if first[i] == last[i]:
            ans.append(first[i])
        else:
            break
    
    return ''.join(ans)

def sol_2(arr: list[str]):
    ans = []
    flag = False
    min_len_str = min(arr, key=len)
    for j in range(len(min_len_str)):
        cur = arr[0][j]
        for i in range(1, len(arr)):
            if arr[i][j] != cur:
                flag = True
                break
        if flag == True:
            break
        else:
            ans.append(cur)
    return ''.join(ans)


print(sol_2(["flower","flow","flight"]))