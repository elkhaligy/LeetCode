def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    length = len(s)

    for _ in range(length):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False

print(rotateString(s = "abcde", goal = "cdeab"))
