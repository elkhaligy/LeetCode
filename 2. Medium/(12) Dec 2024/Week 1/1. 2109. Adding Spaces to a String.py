def addSpace(s: str, spaces: list[int]):
    newStr = ""
    spacesSet = set(spaces)
    for index, char in enumerate(s):
        if index in spacesSet:
            newStr += " "
        newStr += char
        
    return newStr

def addSpaceSol2(s: str, spaces: list[int]):
    newStr = ""
    curIndex = 0
    for spaceIndex in spaces:
        newStr += s[curIndex:spaceIndex] + " "
        curIndex = spaceIndex
    newStr += s[curIndex:]
        
    return newStr
print(addSpaceSol2(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))