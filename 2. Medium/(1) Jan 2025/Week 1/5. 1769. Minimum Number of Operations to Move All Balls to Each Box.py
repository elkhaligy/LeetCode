def minOperations(boxes: str) -> list[int]:
    n = len(boxes)
    answer = [0] * n

    ballsLeft = 0
    ballsRight = 0
    movesLeft = 0
    movesRight = 0

    for i in range(n):
        answer[i] += movesLeft
        ballsLeft += int(boxes[i])
        movesLeft += ballsLeft
        j = n - 1 - i
        answer[i] += movesRight
        ballsRight += int(boxes[j])
        movesRight += ballsRight

    return answer


print(minOperations(boxes = "110"))
