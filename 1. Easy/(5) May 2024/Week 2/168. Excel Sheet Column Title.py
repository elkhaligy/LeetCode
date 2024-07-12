def convertToTitle(columnNumber: int) -> str:
    ans = []
    while columnNumber:
        remainder = columnNumber % 26
        # Special case if remander == 0
        if remainder == 0:
            remainder = 26
            columnNumber -= 1
        ans.append(chr(remainder + ord('A') - 1))
        columnNumber = columnNumber // 26

    return ''.join(ans[::-1])

def convertToTitleSol2(columnNumber: int) -> str:
    ans = ""
    while columnNumber > 0:
        columnNumber -=  1
        ans = chr(columnNumber % 26 + ord('A')) + ans
        columnNumber //= 26

    
    print(ans)
print(convertToTitleSol2(27))
