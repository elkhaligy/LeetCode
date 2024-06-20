from collections import Counter

def minWindow(s: str, t: str) -> str:
    if len(t) == 1 or len(t) == 0:
        if t in s:
            return t
        else:
            return ""
        
    t_map = Counter(t)
    w_map = {key: 0 for key in t_map.keys()}

    have, need = 0, len(t_map)
    have_flag = False
    left, right = 0, 0
    ans = (0, len(s) - 1)

    while right < len(s):

        if s[right] in t_map:
            w_map[s[right]] += 1

            if w_map[s[right]] == t_map[s[right]]:
                have += 1

        while have == need:
            have_flag = True
            ans = (left, right) if (ans[1] - ans[0] + 1) > (right - left + 1) else (ans[0], ans[1])

            if s[left] in w_map:
                w_map[s[left]] -= 1
                if w_map[s[left]] < t_map[s[left]]:
                    have -= 1
            left += 1

        right += 1

    if not have_flag:
        return ""
    else:
        return s[ans[0]:ans[1] + 1]

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))