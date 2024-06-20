def can_be_positioned(positions: list[int], mid: int, m: int) -> bool:
    previous_pos = positions[0]
    placed_balls = 1

    for i in range(1, len(positions)):
        current_pos = positions[i]
        if current_pos - previous_pos >= mid:
            placed_balls += 1
            previous_pos = positions[i]

        if placed_balls == m:
            return True

    return False    

def maxDistance(position: list[int], m: int) -> int:
    n = len(position)
    position.sort()

    left = 1
    right = position[-1]
    max_dist = 0

    while left <= right:
        mid = left + (right - left) // 2
        if can_be_positioned(position, mid, m):
            max_dist = max(max_dist, mid)
            left = mid + 1
        else:
            right = mid - 1

    return max_dist

print(maxDistance(position = [79,74,57,22], m = 4))
