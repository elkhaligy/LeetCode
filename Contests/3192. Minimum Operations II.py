def minOperations(nums: list[int]) -> int:
    answer = 0
    flipped = [float('inf'), 0]
    # start index, end index, number of flips
    for i in range(len(nums)):
        if nums[i] == 0 and i >= flipped[0] and flipped[1] % 2 == 1:
            continue
        if nums[i] == 0 and i >= flipped[0]:
            flipped[0] = i
            flipped[1] += 1
            answer += 1
        elif nums[i] == 1 and i < flipped[0] or (i >= flipped[0] and flipped[1] % 2 == 0):
            continue
        else:
            flipped[0] = i
            flipped[1] += 1
            answer += 1

    return answer

print(minOperations(nums = [0,1,1,0,1]))