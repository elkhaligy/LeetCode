def maximumGain_bruteforce(s: str, x: int, y: int) -> int:
    first, second = ('ab', 'ba') if x >= y else ('ba', 'ab')
    max_gain, min_gain = max(x, y), min(x, y)
    ans = 0

    while s.count('ab') or s.count('ba'):
        while s.count(first):
            s = s.replace(first,"",1)
            ans += max_gain
        while s.count(second):
            s = s.replace(second,"",1)
            ans += min_gain

    return ans 

def maximumGain_stack_optimized(s: str, x: int, y: int) -> int:
    # Greedly detect best pattern
    first, second = ('ab', 'ba') if x >= y else ('ba', 'ab')
    max_gain, min_gain = max(x, y), min(x, y)
    
    # Calculate the gain by specific pattern in a specific string in only O(n)
    def get_gain(string: str, pattern: str, gain: int) -> tuple[int, str]:
        ans = 0
        stack = []

        for chr in string:
            if stack and stack[-1] + chr == pattern:
                ans += gain
                stack.pop()
            else:
                stack.append(chr)

        return ans, "".join(stack)

    # Optain first and second gain
    first_gain, remaining_str = get_gain(s, first, max_gain)
    second_gain, _ = get_gain(remaining_str, second, min_gain)

    # Return the sum of both gains
    return first_gain + second_gain

print(maximumGain_stack_optimized(s = "aabbaaxybbaabb", x = 5, y = 4))
