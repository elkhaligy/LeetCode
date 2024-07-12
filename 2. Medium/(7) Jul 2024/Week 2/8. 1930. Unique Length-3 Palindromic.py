def countPalindromicSubsequence(s: str) -> int:
    checked = set()
    ans = 0
    n = len(s)

    for i in range(n):
        if s[i] in checked:
            continue

        between = set()
        checked.add(s[i]) 
        left_occu = i
        right_occu = s.rindex(s[i])

        for j in range(left_occu + 1, right_occu):
            between.add(s[j])
        if right_occu - left_occu + 1 >= 3:
            ans += len(between)

    return ans

def countPalindromicSubsequence_sol2(s: str) -> int:
    s_unq = set(s)
    ans = 0
    n = len(s_unq)

    for ch in s_unq:
        between = set()
        left_occu = s.index(ch)
        right_occu = s.rindex(ch)

        for j in range(left_occu + 1, right_occu):
            between.add(s[j])
        ans += len(between)

    return ans
print(countPalindromicSubsequence(s = "bbcbaba"))