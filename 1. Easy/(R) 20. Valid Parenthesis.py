def isValid(s: str) -> bool:
    stack = []
    equi_dict = {')':'(', '}':'{', ']':'['}
    for paren in s:
        if paren not in equi_dict:
            stack.append(paren)
        elif paren in equi_dict and len(stack) != 0:
            cur_paren = stack.pop()
            if cur_paren != equi_dict[paren]:
                return False
        else:
            return False
                
    return len(stack) == 0

def isValid_refactored(s: str) -> bool:
    stack = []
    matching_parenthesis = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    
    for char in s:
        if char in matching_parenthesis:
            if stack and stack[-1] == matching_parenthesis[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack

print(isValid_refactored('[([)])]'))
        