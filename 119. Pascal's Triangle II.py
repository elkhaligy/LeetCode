def generate(numRows: int) -> list[list[int]]:
    ans = []
    numRows += 1
    for i in range(numRows):
        a = [0] * (i + 1)
        ans.append(a)
    for i in range(numRows):
        ans[i][0] = 1
    for i in range(numRows):
        ans[i][-1] = 1

    for i in range(2, numRows):
        for j in range(1, i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]


    return ans[numRows-1]


print(generate(1))