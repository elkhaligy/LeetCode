def addDigits(num: int) -> int:

    def rec(num):
        s = str(num)
        ans = 0
        for c in s:
            ans += int(c)
        if len(str(ans)) == 1:
            return ans
        return rec(ans)

    return rec(num)

print(addDigits(0))
