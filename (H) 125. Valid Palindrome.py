# isalpha() and isdigit() can be both compined in isalnum()
def isPalindrome(s: str) -> bool:
    new_str = []
    for c in s:
        if c.isalpha() or c.isdigit():
            new_str.append(c.lower())
    
    ans = ''.join(new_str)
    return ans == ans[::-1]

def isPalindrome_Sol2(s: str) -> bool:
    left = 0
    right = len(s) - 1
    s = s.lower()
    while left < right:
        while not(s[left].isalpha or s[left].isdigit()) and left < right:
            left += 1
        while not(s[right].isalpha() or s[right].isdigit()) and right > left:
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1
    return True

def isPalindrome_Sol3(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
print(isPalindrome_Sol2(s = ".,"))