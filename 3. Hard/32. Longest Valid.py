def longestValidParentheses(s: str) -> int:
    stack = []
    zero_one_list = [0] * len(s)
    matching_parenthesis = {
        ')':'(',
    }
    
    for index, char in enumerate(s):
        if char in matching_parenthesis:
            if stack and stack[-1][0] == matching_parenthesis[char]:
                popped = stack.pop()
                zero_one_list[popped[1]] = 1
                zero_one_list[index] = 1
            else:
                continue
        else:
            stack.append( (char, index) )
            
    # Longest continous 1
    longest_ones = 0
    longest_ones_sofar = 0
    for num in zero_one_list:
        if num == 0:
            longest_ones_sofar = max(longest_ones_sofar, longest_ones)
            longest_ones = 0
        else:
            longest_ones += 1
        longest_ones_sofar = max(longest_ones_sofar, longest_ones)
    return longest_ones_sofar
# ())()
print(longestValidParentheses(s = "()(()"))