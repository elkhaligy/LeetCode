from collections import Counter
def longestPalindrome(s: str) -> int:
    chars_cntr = Counter(s)
    ans = []
    #print(chars_cntr)
    for key, value in chars_cntr.items():
        while value >= 2:
            ans.append(key)
            ans.insert(0, key)
            value -= 2
            chars_cntr[key] = value
    
    #print(ans)
    longest = len(ans)
    for value in chars_cntr.values():
        if value == 1:
            longest += 1
            break

    return longest


def longestPalindrome_optimized(s: str) -> int:
    chars_cntr = Counter(s)
    longest = 0

    for key, value in chars_cntr.items():
        longest += (value // 2) * 2
        chars_cntr[key] -= (value // 2) * 2
    
    for value in chars_cntr.values():
        if value == 1:
            longest += 1
            break

    return longest

def longestPalindrome_karim(s: str) -> int:
    
    dictt={}
    for i in s:
        if i in dictt:
            dictt[i]+=1
        else:
            dictt[i]=1
    j=0
    #print(dictt)
    maxx_odd=0
    summ_even=0
    for i in dictt.values():
        if i%2==0:
            summ_even+=i
            j+=1
        else:
            if maxx_odd<i:
                maxx_odd=i

    if j==len(dictt):
        return summ_even
    elif j==0:
        return maxx_odd
    else:
        return summ_even+ maxx_odd

s = "rqsczzzssadfft"
print("me", longestPalindrome_optimized(s))
print("karim",longestPalindrome_karim(s))