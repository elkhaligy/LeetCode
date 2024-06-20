def generate(numRows: int) -> list[list[int]]:
    ans = []

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


    return ans

def generate_Sol2(numRows: int) -> list[list[int]]:
    ans = []

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


    return ans
print(generate(5))