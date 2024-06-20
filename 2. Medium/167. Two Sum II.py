def twoSum_hashmap(numbers, target):
    hashTable = {}

    for i in range(len(numbers)):
        # target = number1 + number2, number2 = target - number1
        if numbers[i] in hashTable:
            return [hashTable[numbers[i]]+1,i+1]
        hashTable[target-numbers[i]] = i
    
def twoSum_twoPointers(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    left = 0
    right = n - 1

    while left < right:
        cur_sum = numbers[left] + numbers[right]
        if cur_sum == target:
            return [left + 1, right + 1]
        elif cur_sum > target:
            right -= 1
        else:
            left += 1

print(twoSum_twoPointers(numbers = [2,7,11,15], target = 9))
