def wordPattern(pattern: str, s: str) -> bool:
    patterns_uniq = []
    s = s.split()
    s_uniq = []
    for chr in pattern:
        if chr in patterns_uniq:
            continue
        patterns_uniq.append(chr)
    for chr in s:
        if chr in s_uniq:
            continue
        s_uniq.append(chr)

    equivalent_dict = {} 
    for char in patterns_uniq:
        equivalent_dict[char] = char
    
    for item in list(zip(patterns_uniq, s_uniq)):
        equivalent_dict[item[0]] = item[1]
    
    ans = []
    for c in pattern:
        ans.append(equivalent_dict[c])
    print(ans)
    return ans == s

print(wordPattern(pattern = "abba", s = "dog cat cat dog"))