def binary_search(l, r):
    if l > r:
        return -1
    mid = (l + r) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(mid + 1,r)
    elif nums[mid] > target:
        return binary_search(l, mid - 1)
    
    



target = 1
nums = [1,3,5,6]
a = binary_search(0, len(nums) - 1)

print(a)