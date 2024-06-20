def romanToInt(s: str) -> int:
    ans = 0
    dct = {'I' : 1,
           'V' : 5,
           'X' : 10,
           'L' : 50,
           'C' : 100,
           'D' : 500,
           'M' : 1000
           }
    reversed_s = s[::-1]
    prev = reversed_s[0]
    ans += dct[prev]
    for c in reversed_s[1:]:
        if (prev == 'V' or prev == 'X') and c == 'I':
            ans -= dct[c]
        elif (prev == 'L' or prev == 'C') and c == 'X':
            ans -= dct[c]
        elif (prev == 'D' or prev == 'M') and c == 'C':
            ans -= dct[c]
        else:
            ans += dct[c]
        prev = c
    return ans

print(romanToInt('IV'))