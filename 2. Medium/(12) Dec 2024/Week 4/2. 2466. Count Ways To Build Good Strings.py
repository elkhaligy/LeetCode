def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    mod = 10 ** 9 + 7
    answer = 0
    memo = {}

    def recur(currLen):
        if currLen > high:
            return 0
        if currLen in memo:
            return memo[currLen]
        
        count = 0
        if low <= currLen <= high:
            count += 1
        
        count += recur(currLen + zero) + recur(currLen + one)
        memo[currLen] = count % mod
        return memo[currLen]

    return recur(0) 
print(countGoodStrings(low = 3, high = 3, zero = 1, one = 1))
