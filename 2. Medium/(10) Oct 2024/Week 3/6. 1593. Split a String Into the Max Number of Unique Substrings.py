def maxUniqueSplit(s: str) -> int:
    n = len(s)
    seen = set()


    def backtrack(start):
        if start == n:
            return 0
        
        max_count = 0

        for end in range(start + 1, n + 1):
            sub_string = s[start:end]
            print(sub_string)
            if sub_string not in seen:
                seen.add(sub_string)
                max_count = max(max_count, 1 + backtrack(end))
                seen.remove(sub_string)

        return max_count

    return backtrack(0)

print(maxUniqueSplit(s = "abac"))