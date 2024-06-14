
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
def rec1(row, col, path):
    node = triangle[row][col]
    path.append(node)
    if row == len(triangle) - 1:
        print(path)
        a = node
        path.pop()
        return a
    rec1(row + 1, col, path)
    rec1(row + 1, col + 1, path)
    path.pop()

def rec2(row, col, sum):
    sum += triangle[row][col]
    if row == len(triangle) - 1:
        return sum

    sum_1 = rec2(row + 1, col, sum)
    sum_2 = rec2(row + 1, col + 1, sum)

    return min(sum_1, sum_2)

print(rec2(0, 0, 0))