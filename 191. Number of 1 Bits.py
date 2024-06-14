from collections import Counter
def hammingWeight(n: int) -> int:
    bin_rep = bin(n)[2:]
    freq_dict = Counter(bin_rep)
    return freq_dict['1']

# Better complexity solution
def hammingWeight_Sol2(n: int) -> int:
    ans = 0
    for i in range(32):
        if n >> i & 1:
            ans += 1
    return ans
print(hammingWeight_Sol2(11))