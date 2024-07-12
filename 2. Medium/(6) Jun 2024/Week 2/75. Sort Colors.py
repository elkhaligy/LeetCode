from collections import Counter
def sortColors(nums: list[int]) -> None:
    start = 0
    end = len(nums) - 1
    middle = 0

    while middle <= end:
        if nums[start] == 2:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
        elif nums[middle] == 2:
            nums[middle], nums[end] = nums[end], nums[middle]
            end -= 1
        elif nums[start] == 0:
            start += 1
            middle += 1
        elif nums[start] == 1 and nums[middle] != 0:
            middle += 1
        else:
            nums[start], nums[middle] = nums[middle], nums[start]
            start += 1
    print(nums)
def sortColors_Sol2(nums: list[int]) -> None:
    occu_dict = Counter(nums)
    for i in range(len(nums)):
        if occu_dict[0] > 0:
            nums[i] = 0
            occu_dict[0] -= 1 
        elif occu_dict[1] > 0:
            nums[i] = 1
            occu_dict[1] -= 1 
        else:
            nums[i] = 2
            occu_dict[2] -= 1 

def sortColors_sol3(nums: list[int]) -> None:
    frequency_counter = {
        0 : 0,
        1 : 0,
        2 : 0
    }
    for num in nums:
        frequency_counter[num] += 1
    
    #print(frequency_counter)
    current_index = 0
    for num, frequency in frequency_counter.items():
        while frequency:
            nums[current_index] = num
            frequency -= 1
            current_index += 1
    
    #print(nums)
# 1, 0 , 2
print(sortColors_sol3( nums = [2,0,2,1,1,0]))