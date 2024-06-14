def maximum69Number(num: int) -> int:
    num = list(str(num))
    for i, digit in enumerate(num):
        if digit == '6':
            num[i] = '9'
            break
    return ''.join(num)

def maximum69Number_sol2(num: int) -> int:
    num = str(num)
    ans = ""
    flag = False
    for i, digit in enumerate(num):
        if digit == '9':
            ans += digit
        else:
            if not flag:
                ans += '9'
                flag = True
            else:
                ans += '6'

    return ans

def maximum69Number_sol3(num: int) -> int:
    return int(str(num).replace('6', '9', 1))

print(maximum69Number_sol3(num = 9669))
