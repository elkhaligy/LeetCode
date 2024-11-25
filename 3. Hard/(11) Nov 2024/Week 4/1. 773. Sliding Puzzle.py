from collections import deque
def slidingPuzzle(board: list[list[int]]) -> int:
    # Direction map key -> zero index : value -> list of available indexes
    directions = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

    def _swap(state: str, zeroIndex, targetIndex):
        stateList = list(state)
        stateList[zeroIndex], stateList[targetIndex] = stateList[targetIndex], stateList[zeroIndex]
        return "".join(stateList)

    targetState = "123450"
    startState = ""
    for row in range(len(board)):
        for col in range(len(board[0])):
            startState += str(board[row][col])
        

    visited = set()
    queue = deque([startState])
    visited.add(startState)
    currentLevel = 0

    # Start BFS Algorithm
    while queue:
        for _ in range(len(queue)):
            currentState = queue.popleft()

            # Check if we reached the target solved state
            if currentState == targetState:
                return currentLevel

            currentZeroIndex = currentState.index("0")
            for neighborIndex in directions[currentZeroIndex]:
                newState = _swap(currentState, currentZeroIndex, neighborIndex)

                if newState in visited:
                    continue

                visited.add(newState)
                queue.append(newState)
        currentLevel += 1

    return -1








    return

print(slidingPuzzle(board = [[4,1,2],[5,0,3]]))
