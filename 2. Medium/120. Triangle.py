def minimumTotal_dp(triangle: list[list[int]]) -> int:
    lst = [[float('inf') for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
    #print(lst)
    lst[0][0] = triangle[0][0]
    
    level = 2
    for i in range(1, len(triangle)):
        for j in range(level):
            # if element is on left
            if j == 0:
                lst[i][j] = triangle[i][j] + lst[i - 1][j]
            # if element is on mid or right
            if j > 0:
                lst[i][j] = min(triangle[i][j] + lst[i - 1][j], triangle[i][j] + lst[i - 1][j - 1])
        level += 1
    return min(lst[-1])

print(minimumTotal_dp(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))