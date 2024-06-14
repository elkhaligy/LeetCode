def niceTeams (minDef, rating):
    hashTable = {}
    for i in range(len(rating)):
        hashTable[minDef + rating[i]] = i
    
    cnt = 0
    for i in range(len(rating)):
        if rating[i] in hashTable:
            cnt += 1
    print (cnt)

niceTeams (4,[6,3,4,5,2,1,1,3])