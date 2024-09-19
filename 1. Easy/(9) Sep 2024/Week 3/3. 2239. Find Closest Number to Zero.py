def findClosestNumber_nlogn(nums: list[int]) -> int:
    nums.sort()
    cur_distance = float('inf')
    for num in nums:
        distance = abs(num)
        if distance < cur_distance:
            cur_distance = distance
            result = num
    
    return result

def findClosestNumber_n(nums: list[int]) -> int:
    cur_distance = float('inf')
    result = float('-inf')
    for num in nums:
        distance = abs(num)
        if distance <= cur_distance:
            cur_distance = distance
            if abs(result) == abs(num):
                result = num if num > result else result
            else:
                result = num
    
    return result
print(findClosestNumber_n(nums = [-4,-2,1,4,8]))
