def minAddToMakeValid(s: str) -> int:
    stack = []
    closing = 0

    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                closing += 1
    return len(stack) + closing



print(minAddToMakeValid(s = ")" ))