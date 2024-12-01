def checkIfExist(arr: list[int]) -> bool:
    currSet = set()

    for num in arr:
        if num * 2 in currSet or (num % 2 == 0 and num // 2 in currSet):
            return True
        currSet.add(num)
    
    return False

def checkIfExistSol2(arr: list[int]) -> bool:
    arrSet = set(arr)
    zeroCount = 0

    for num in arr:
        if num == 0:
            zeroCount += 1
    if zeroCount > 1:
        return True
    
    for num in arrSet:
        if num != 0 and num * 2 in arrSet:
            return True
    return False