# https://github.com/kilian-hu/hackerrank-solutions/tree/master/certificates/problem-solving-intermediate/sorted-sums

def sortedSums(arr):
    ans = 0
    for i in range(len(arr)):
        sub = arr[0:i+1]
        sub.sort()
        for i in range(len(sub)):
            ans += (i+1) * sub[i]
     
        print(sub)
    print(ans)

sortedSums([5,9])