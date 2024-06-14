def isPalindrome(x: int) -> bool:
    x = str(x)
    n = len(x)
    if n == 1:
        return True
    left = 0
    right = n - 1
    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome(12231))