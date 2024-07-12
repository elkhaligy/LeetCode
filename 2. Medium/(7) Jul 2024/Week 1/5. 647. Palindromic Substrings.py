def countSubstrings_bruteforce_TLE_oN3(s: str) -> int:
    def is_palindrome(s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
    answer = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i: j + 1]):
                answer += 1
    
    return answer

def countSubstrings_expandMiddle_oN2(s: str) -> int:
    n = len(s)
    answer = 0

    def count_palindromes(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count
    for i in range(n):
        # Even palindromes
        # aaa
        # first (a) -> aa 1
        # second (a) -> aa 2
        # Odd palindromes
        # aaa
        # first (a) -> a 3
        # second (a) -> a 4-> a a a 5
        # third (a) -> a 6
        even_palindromes = count_palindromes(i, i + 1)
        odd_palindromes = count_palindromes(i, i)
        answer += even_palindromes + odd_palindromes

    return answer
print(countSubstrings_expandMiddle_oN2(s= "abc"))