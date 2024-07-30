# Need to add more solutions
def minimumDeletions(s: str) -> int:
    n = len(s)
    a_after = [0] * n
    b_before = [0] * n

    a_counter = 0
    for i in range(n - 1, -1, -1):
        a_after[i] = a_counter
        if s[i] == 'a':
            a_counter += 1

    b_counter = 0
    for i in range(n):
        b_before[i] = b_counter
        if s[i] == 'b':
            b_counter += 1
    
    ans = float('inf')
    for i in range(n):
        ans = min(ans, a_after[i] + b_before[i])

    return ans

print(minimumDeletions(s = "aababbab"))
