def canBeValid_189testcases(s: str, locked: str) -> bool:
    stack = []
    n = len(s)
    if n == 1 or n % 2 != 0:
        return False
    
    for i, paren in enumerate(s):
        if paren == '(':
            stack.append((paren, i))
        elif paren == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                if locked[i] == '0':
                    stack.append(('(', i))
                else:
                    return False
                
    if len(stack) >= 2:
        while len(stack):
            first_paren = stack.pop()
            second_paren = stack.pop()
            #print(locked[first_paren[1]])
            if locked[first_paren[1]] == '1':
                return False   
            #print(first_paren, second_paren)
    return len(stack) == 0
#second( first(

def canBeValid(s: str, locked: str) -> bool:
    stack = []
    n = len(s)
    if n == 1 or n % 2 != 0:
        return False
    if s[0] == ')' and locked[0] == '1':
        return False
    if s[-1] == '(' and locked[-1] == '1':
        return False
    
    flag = False
    for i, p in enumerate(s):
        if locked[i] == '0':
            stack.append('0')
        elif p == '(':
            stack.append(p)
        elif p == ')':
            for k in range(len(stack) - 1, -1, -1):
                if stack[k] == '(':
                    stack.pop(k)
                    flag = True
                    break
            if not flag:
                stack.pop()
            flag = False
    #print(len(stack))


    no_zeros = 0
    if len(stack) == 0:
        return True
    else:
        while len(stack):
            first = stack.pop()
            if first == '0':
               no_zeros += 1
            elif first == '(':
                no_zeros -= 1
                if no_zeros < 0:
                    return False
                
    return True
    #return stack[0] == '0' and stack[-1] == '0'
#second( first(

print(canBeValid(s = "()))(()(()()()()(((())())((()((())" ,locked = "1100000000000010000100001000001101"))