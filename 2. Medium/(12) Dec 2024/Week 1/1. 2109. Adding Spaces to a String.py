def addSpace(s: str, spaces: list[int]):
    newStr = ""
    spacesSet = set(spaces)
    for index, char in enumerate(s):
        if index in spacesSet:
            newStr += " "
        newStr += char
        
    return newStr

print(addSpace(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))