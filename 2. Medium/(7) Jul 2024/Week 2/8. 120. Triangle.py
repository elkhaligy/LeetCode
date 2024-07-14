def minimumTotal_bruteforce(triangle: list[list[int]]) -> int:
    row_len = len(triangle)
    counter = 1
    def recursive(row: int, col: int) -> int:
        nonlocal counter

        if row >= row_len:
            return 0

        print(f"{counter}: In Node -> {triangle[row][col]}")
        counter += 1

        return triangle[row][col] + min(recursive(row + 1, col), recursive(row + 1, col + 1))
    
    ans: int = recursive(0, 0)

    return ans
    # What do you need for a recursive function
    # - returns: integer which is minimum path sum of left and right
    # - takes: row and column that represents the element 1
    # - recurrence relation: recursive(node) = node + min(recursve(node.left), recursive(node.right))
    # - base case: last row
    # - base case returns: 0

#    2
#   3 4
#  6 5 7
# 4 1 8 3
def minimumTotal_dp_topdown(triangle: list[list[int]]) -> int:
    # it is called topdown because you start breaking the big problem into subproblems
    row_len = len(triangle)
    remembrance_dict = {}

    def recursive(row: int, col: int) -> int:
        if row >= row_len:
            return 0
        if (row, col) in remembrance_dict:
            return remembrance_dict[(row, col)]
        remembrance_dict[(row, col)] = triangle[row][col] + min(recursive(row + 1, col), recursive(row + 1, col + 1))
        return remembrance_dict[(row, col)]
    
    ans: int = recursive(0, 0)

    return ans

def minimumTotal_dp_bottomup(triangle: list[list[int]]) -> int:
    dp = triangle[-1]

    # Start from the second to last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

    return dp[0]
#    2
#   3 4
#  6 5 7
# 4 1 8 3
print(minimumTotal_dp_bottomup(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))