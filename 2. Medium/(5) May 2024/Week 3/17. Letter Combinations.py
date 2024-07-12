import itertools
def letterCombinations(digits: str) -> list[str]:
    res = []
    def backtrack(idx, comb):
        if idx == len(digits):
            res.append(comb[:])
            return
        
        for letter in dct[digits[idx]]:
            comb.append(letter)
            backtrack(idx + 1, comb)
            comb.pop()

    backtrack(0, [])
    return res

dct = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
}
print(letterCombinations('23'))