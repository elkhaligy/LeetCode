def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    for i in range(m, m + n):
        nums1[i] = nums2[j]
        j += 1
    
    nums1.sort()

num1 = [1,2,3,0,0,0]
merge(num1, 3, [2,5,6], 3)

print(num1)