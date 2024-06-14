from collections import Counter
def groupAnagrams(strs: list[str]):
    dct = {}
    #'key: word': 'value: list of strings'
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dct:
            dct[sorted_word].append(word)
        else:
            dct[sorted_word] = []
            dct[sorted_word].append(word)
    ans = []
    for values in dct.values():
        ans.append(values)
    return ans




print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
