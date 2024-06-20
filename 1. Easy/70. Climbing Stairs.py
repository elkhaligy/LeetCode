def climbStairs_recursive_bruteforce(self, n: int) -> int:
    def rec(n):
        print(n)
        if n <= 1:
            return 1
        else:
            return rec(n - 1) + rec(n - 2)
            
def climbStairs_dp_memoization(n: int) -> int:
    i = n
    mem = {}

    def rec(i):
        if i <= 1:
            return 1
        else:
            if i in mem:
                return mem[i]
            mem[i] = rec(i - 1) + rec(i - 2)
            return mem[i]
    
    return rec(i)

def climbStairs_dp(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    lst = [0] * (n + 1)
    lst[1] = 1
    lst[2] = 2

    for i in range(3, n + 1):
        lst[i] = lst[i - 1] + lst[i -2]
    
    return lst[-1]

print(climbStairs_dp(n = 2))