def isPowerOfFour(n: int) -> bool:

    def rec(a):
        if 4 ** a == n:
            return True
        if 4 ** a > n:
            return False
        
        return rec(a + 1)
    return rec(0)


print(isPowerOfFour(16384))
