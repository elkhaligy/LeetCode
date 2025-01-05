def shiftingLetters_TLE(s: str, shifts: list[list[int]]) -> str:
    # Brute force solution 
    # loop through each shift and apply it
    # For each shift
        # loop through the string from start to end inclusive
        # for each character shift it foward or backward depending on the direction
    letters = list(s)
    for shft in shifts:
        for i in range(shft[0], shft[1] + 1):
            if shft[2] == 1:
                if letters[i] == 'z':
                    letters[i] = 'a'
                else:
                    letters[i] = chr(ord(letters[i]) + 1)
            else:
                if letters[i] == 'a':
                    letters[i] = 'z'
                else:
                    letters[i] = chr(ord(letters[i]) - 1)

    return "".join(letters)

def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    # Use difference array to update a range in only o(n)
    n = len(s)
    diffArr = [0] * n
    letters = list(s)
    for shft in shifts: 
        if shft[2] == 1:
            diffArr[shft[0]] += 1
            if shft[1] + 1 < n:
                diffArr[shft[1] + 1] -= 1
        else:
            diffArr[shft[0]] -= 1
            if shft[1] + 1 < n:
                diffArr[shft[1] + 1] += 1
    # print(diffArr)

    relativeArr = [0] * n
    relativeArr[0] = diffArr[0]
    for i in range(1, n):
        relativeArr[i] = relativeArr[i - 1] + diffArr[i]
    # print(relativeArr) 

    shifts = 0
    for i in range(n):
        shifts = relativeArr[i]
        if shifts < 0:
            shifts += 26
        newChr = chr((ord(s[i]) - ord("a") + shifts) % 26 + ord("a"))
        letters[i] = newChr
            
    return "".join(letters)


print(shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]))