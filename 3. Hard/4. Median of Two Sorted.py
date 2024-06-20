def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums1_pointer = 0
    nums2_pointer = 0
    merged_list = []

    while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
        if nums1[nums1_pointer] < nums2[nums2_pointer]:
            merged_list.append(nums1[nums1_pointer])  
            nums1_pointer += 1
        else:
            merged_list.append(nums2[nums2_pointer])
            nums2_pointer += 1

    while nums1_pointer < len(nums1):
        merged_list.append(nums1[nums1_pointer])
        nums1_pointer += 1
    
    while nums2_pointer < len(nums2):
        merged_list.append(nums2[nums2_pointer])
        nums2_pointer += 1

    if len(merged_list) % 2 == 0:
        return (merged_list[len(merged_list) // 2] + merged_list[len(merged_list) // 2 - 1]) / 2
    else:
        return float(merged_list[len(merged_list) // 2])


print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
