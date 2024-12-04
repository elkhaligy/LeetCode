def isSubsequent(str1: str, str2: str):
    p1 = p2 = 0

    # chr((ord('z') - ord('a') + 1) % 26 + ord('a'))

    while p1 < len(str1) and p2 < len(str2):
        if (
            str1[p1] == str2[p2]
            or chr((ord(str1[p1]) - ord("a") + 1) % 26 + ord("a")) == str2[p2]
        ):
            p1 += 1
            p2 += 1
        else:
            p1 += 1

    return p2 == len(str2)


def isSubsequentSol2(str1: str, str2: str):
    p1 = p2 = 0

    while p1 < len(str1) and p2 < len(str2):
        if str1[p1] == str2[p2] or abs(ord(str1[p1]) - ord(str2[p2])) == 1:
            p1 += 1
            p2 += 1
        else:
            p1 += 1

    return p2 == len(str2)


def isSubsequentSol3(str1: str, str2: str):
    p1 = p2 = 0
    if len(str2) > len(str1):
        return False

    for p1 in range(len(str1)):
        if p2 < len(str2) and ord(str2[p2]) in (
            ord(str1[p1]),
            ord(str1[p1]) + 1,
            ord(str2[p1]) - 25,
        ):
            p1 += 1
            p2 += 1
            if p2 == len(str2):
                return True
        else:
            p1 += 1

    return p2 == len(str2)


def isSubsequentSol4(str1: str, str2: str):
    p1 = p2 = 0
    str1Len = len(str1)
    str2Len = len(str2)
    if str2Len > str1Len:
        return False

    for chr in str1:
        ordVal = ord(chr)
        if p2 < str2Len and chr == str2[p2] or ordVal - ord(str2[p2]) == -1 or ordVal - ord(str2[p2]) == 25:

            p2 += 1
            if p2 == str2Len:
                return True

    return p2 == str2Len


print(isSubsequent(str1="a", str2="d"))
