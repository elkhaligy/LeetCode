def permuteUnique(nums: list[int]) -> list[list[int]]:
    result_lst = []
    
    def backtracking(current_lst: list[int], taken_indices) -> None:
        if len(current_lst) == len(nums):
            if current_lst in result_lst:
                return
            result_lst.append(current_lst[:])
            return

        for idx, num in enumerate(nums):
            if idx in taken_indices:
                continue
            current_lst.append(num)
            taken_indices.add(idx)
            backtracking(current_lst, taken_indices)
            taken_indices.remove(idx)
            current_lst.pop() 

    backtracking([], set())
    return result_lst
def nextPermutation_timelimit(nums: list[int]) -> None:
    result_list = permuteUnique(sorted(nums))

    # for index, item in enumerate(result_list):
    #     if item == nums:
    #         return result_list[index + 1] if index + 1 < len(result_list) else result_list[0]

    for index, item in enumerate(result_list):
        print(item)
        if item == nums:
            if index + 1 < len(result_list):

                for i in range(len(nums)):
                    nums[i] = result_list[index + 1][i]
            else:
                #nums = result_list[0]
                for i in range(len(nums)):
                    nums[i] = result_list[0][i]
            break

def nextPermutation_optimized_50testcases(nums: list[int]) -> None:
    n = len(nums)
    if n == 1:
        return nums
    if n == 2:
        nums[0], nums[1] = nums[1], nums[0]
        return

    right = n - 1
    largest = []
    largest = nums[right]
    largest_index = right
    for i in range(right, -1, -1):
        if nums[i] >= largest:
            largest = nums[i]
            largest_index = i
    #print(largest, largest_index)

    if largest_index != 0:
        my_window = (largest_index - 1, right)
    else:
        my_window = (largest_index + 1, right)

    for i in range(my_window[0], my_window[1] + 1):
        if nums[i] == 0:
            my_window = i + 1, right
            break
    # find the next greater for the first index
    prev_val = 1000
    next_greater_index = -1
    for i in range(my_window[0] + 1, my_window[1] + 1):
        if nums[i] - nums[my_window[0]] <= 0:
            continue
        if nums[i] - nums[my_window[0]] <= prev_val:
            next_greater_index = i
        prev_val = nums[i] - nums[my_window[0]]

    if next_greater_index == -1:
        nums.sort()
        return
    nums[my_window[0]], nums[next_greater_index] = nums[next_greater_index], nums[my_window[0]]

    nums[my_window[0] + 1:my_window[1] + 1] = sorted(nums[my_window[0] + 1:my_window[1] + 1])

nums = [2,2,7,5,4,3,2,2,1] # [2,3,1,2,2,2,4,5,7]
nums = [4,2,0,2,3,2,0]

 # [2, 1, 2, 2]
nextPermutation_optimized_50testcases(nums)
print(nums)