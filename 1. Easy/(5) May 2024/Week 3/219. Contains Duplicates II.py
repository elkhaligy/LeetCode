from collections import defaultdict
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    dct = defaultdict(int)
    for index, num in enumerate(nums):
        if num in dct:
            if abs(index - max(dct[num])) <= k:
                return True
            dct[num].append(index)
        else:
            dct[num] = []
            dct[num].append(index)
    return False

        
print(containsNearbyDuplicate(nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
, k = 1))