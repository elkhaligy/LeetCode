def searchRange(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    if n == 0:
        return [-1, -1]
    left = 0
    right = n - 1
    first_index = -1
    last_index = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # obtain first_index
            for i in range(mid, -1, -1):
                if nums[i] == target:
                    first_index = i
                else:
                    break
            # obtain last_index
            for i in range(mid, n):
                if nums[i] == target:
                    last_index = i
                else:
                    break
            break
            
    return [first_index, last_index]  


print(searchRange(nums = [5], target = 5))