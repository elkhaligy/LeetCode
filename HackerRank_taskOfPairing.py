# https://github.com/kilian-hu/hackerrank-solutions/tree/master/certificates/problem-solving-intermediate/task-of-pairing

def taskOfPairing(dmbls):
    ans = 0
    rem = 0
    for i in range(len(dmbls)):

        if dmbls[i] % 2 == 0:
            ans += dmbls[i] // 2
            rem = 0
        else:
            ans += (dmbls[i]-1) // 2
            if rem > 0:
                ans += rem
            else:
                rem += 1

            

    print(ans)
1 + 1 + 2 + 1 + 2 + 1 + 1 
taskOfPairing([5,6,2])