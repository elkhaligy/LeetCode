def defuseTheBomb(code: list[int], k: int):
    if k == 0:
        return [0] * len(code)
    isNegFlag = 0
    if k < 0:
        code = code[::-1]
        isNegFlag = 1
        k *= -1
    
    # Set up initial window
    newCode = [0] * len(code)
    left = right = 1
    curWindowSum = 0
    while right <= k:
        curWindowSum += code[right % len(code)]
        right += 1
    right -= 1

    # Slide the window
    for i in range(len(code)):
        newCode[i] = curWindowSum
        curWindowSum -= code[left % len(code)]
        left += 1
        right += 1
        curWindowSum += code[right % len(code)]
    if isNegFlag:
        return newCode[::-1]
    else:
        return newCode


print(defuseTheBomb(code = [2,4,9,3], k = -2))