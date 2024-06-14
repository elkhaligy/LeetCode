def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    
    def binary_search(nums: list[int]):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return True
        return False
    result = False
    for row in matrix:
        result = result or binary_search(row)
        if result == True:
            break

    return result

print(searchMatrix(matrix = [[1,1,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
