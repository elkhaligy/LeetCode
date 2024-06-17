# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr_builtin(haystack: str, needle: str):
    return haystack.find(needle)

def strStr_nonbuiltin(haystack: str, needle: str):
    for index, letter in enumerate(haystack):
        if letter == needle[0]:
            current_word = haystack[index: index + len(needle)]
            if current_word == needle:
                return index
    return -1

def strStr_nonbuiltin_sol2(haystack: str, needle: str):
    for index in range(len(haystack) - len(needle) + 1):
        current_word = haystack[index : index + len(needle)]
        if current_word == needle:
            return index
    return -1

print(strStr_nonbuiltin_sol2(haystack = "bustedsa", needle = "sad"))        