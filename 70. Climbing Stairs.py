class Solution:
    def climbStairs(self, n: int) -> int:
        
        def brute(n):
            print(n)
            if n <= 1:
                return 1
            else:
                return brute(n - 1) + brute(n - 2)
            
def climbStairs(n: int) -> int:
    i = n
    mem = {}
    def brute(i):
        #print(i)
        if i <= 1:
            return 1
        else:
            if i in mem:
                return mem[i]
            mem[i] = brute(i - 1) + brute(i - 2)
    
            return mem[i]
    ans = brute(i)
    return ans