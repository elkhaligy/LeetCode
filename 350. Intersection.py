from collections import Counter
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    counter_1 = Counter(nums1)
    counter_2 = Counter(nums2)

    for key in counter_1:
        if key not in counter_2:
            counter_1[key] = 0
        else:
            counter_1[key] = min(counter_1[key], counter_2[key])
    
    #print(counter_1)

    result = []
    for key in counter_1:
        for _ in range(counter_1[key]):
            result.append(key)
    
    return result
print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))