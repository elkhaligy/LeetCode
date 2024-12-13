def decodeString(s: str) -> str:
    stack = []
    curNum = 0
    curStr = ''
    ans = ''
    for char in s:
        if char.isdigit():
            curNum = curNum * 10 + int(char)
        elif char == '[':
            stack.append(curNum)
            stack.append(curStr)
            curNum = 0
            curStr = ''
        elif char == ']':
            popStr = stack.pop()
            popNum = stack.pop()
            ans = popStr + int(popNum) * curStr
        else:
            curStr += char
    
    return ans

print(decodeString("3[a]2[bc]"))