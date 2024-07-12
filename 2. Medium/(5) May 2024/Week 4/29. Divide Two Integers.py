def divide(dividend: int, divisor: int) -> int:
    negative_answer = True if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0) else False
    dividend = abs(dividend)
    divisor = abs(divisor)
    if divisor == 1:
        if dividend > ((1 << 31) - 1) and not negative_answer:
            dividend = (1 << 31) - 1
        return dividend if not negative_answer else -dividend
    # dividend = (quotient) * divisor + remainder
    # 10 / 3
    # 10 = (2^1 + 2^0) * 3 + remainder
    # 10 = 2 ^ 1 * 3 + 2 ^ 0 * 3

    
    def rec(dividend, result):
        if dividend < divisor:
            return result
        shift = 1
        aux = divisor
        cnt = 0
        while aux <= dividend:
            aux = divisor << shift
            cnt += 1
            shift += 1
        dividend -= divisor << (cnt - 1)
        return rec(dividend, result + (1 << (cnt - 1)))
    ans = rec(dividend, 0)
    print(ans)
    if ans > ((1 << 31) - 1):
        ans = (1 << 31) - 1
    return ans if not negative_answer else -ans
print(divide(-2147483648, -1))