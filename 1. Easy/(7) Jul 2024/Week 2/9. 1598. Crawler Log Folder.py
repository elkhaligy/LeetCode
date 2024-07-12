def minOperations_sol1(logs: list[str]) -> int:
    ans = 0
    for command in logs:
        if len(command) == 2 and command != "./":
            ans += 1
        elif len(command) > 2:
            cur_com = command[-1] + command[-2] + command[-3]
            if cur_com == "/..":
                ans -= 1
            else:
                ans += 1
        if ans < 0:
            ans = 0

    return ans


def minOperations_sol2(logs: list[str]) -> int:
    hash_table = {
        "../" : -1,
        "./"  : 0,
    }
    ans = 0
    for log in logs:
        if log in hash_table:
            ans += hash_table[log]
        else:
            ans -= 1
        
        if ans < 0:
            ans = 0

    return ans

def minOperations_sol3(logs: list[str]) -> int:
    ans = 0
    for log in logs:
        if log == "./":
            continue
        elif log == "../":
            ans = max(0, ans - 1)
        else:
            ans += 1
    
    return ans

def minOperations_sol4(logs: list[str]) -> int:
    stack = []
    for log in logs:
        if log == "../":
            if stack:
                stack.pop()
        elif log != "./":
            stack.append(log)

    
    return len(stack)
print(minOperations_sol4(logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))
