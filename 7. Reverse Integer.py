def reverse(x: int) -> int:
    negative = False
    answer = 0

    if x < 0:
        x = x * -1
        negative = True

    number_length = len(str(x))

    i = 1
    while x != 0:
        rem = x % 10
        x //= 10
        answer += rem * (10 ** (number_length - i))
        i += 1

    if answer > 2 ** 31 - 1:
        return 0
    if negative:
        answer *= -1
    return answer

def reverse_sol2(x: int) -> int:
    negative_flag = False

    if x < 0:
        negative_flag = True
        x = str(x)[1:]
    else:
        x = str(x)

    x = x[::-1]

    if int(x) > (2 ** 31) -1 or int(x) < - (2 ** 31):
        return 0
    
    return -1 * int(x) if negative_flag else int(x)
print(reverse(x = -123))
            