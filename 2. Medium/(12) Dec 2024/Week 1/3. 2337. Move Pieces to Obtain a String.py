def canChangeSol2(start: str, target: str) -> bool:
    # Construct the list of tuples where element is (chr, index)
    startPositions = []
    targetPositions = []

    for i in range(len(start)):
        if start[i] != "_":
            startPositions.append((start[i], i))
        if target[i] != "_":
            targetPositions.append((target[i], i))

    if len(startPositions) != len(targetPositions):
        return False
    
    #print(startPositions, targetPositions)

    for i in range(len(startPositions)):
        if startPositions[i][0] == 'L':
            if startPositions[i][1] < targetPositions[i][1]:
                return False
        elif startPositions[i][0] == 'R':
            if startPositions[i][1] > targetPositions[i][1]:
                return False
    
    return True

def canChange(start: str, target: str) -> bool:
    # Check order
    startStr = ""
    targetStr = ""
    for c in start:
        if c != "_":
            startStr += c

    for c in target:
        if c != "_":
            targetStr += c
    if startStr != targetStr:
        return False
    startPtr = targetPtr = 0

    while startPtr < len(start) and targetPtr < len(target):
        if target[targetPtr] == '_':
            targetPtr += 1
            continue
        elif target[targetPtr] == 'L':
            while True:
                if start[startPtr] == '_':
                    startPtr += 1
                    continue
                elif start[startPtr] == 'R':
                    return False
                else:
                    if startPtr < targetPtr:
                        return False
                startPtr += 1
                break
        elif target[targetPtr] == 'R':
            while True:
                if start[startPtr] == '_':
                    startPtr += 1
                    continue
                elif start[startPtr] == 'L':
                    return False
                else:
                    if startPtr > targetPtr:
                        return False
                startPtr += 1
                break

            
        targetPtr += 1

    return True



print(canChangeSol2(start = "_L__R__R_", target = "L______RR"))
