def nextGreaterElement_bruteforce(nums1: list[int], nums2: list[int]) -> list[int]:
    n = len(nums2)
    ind_dict = {} # element : index
    ans = []
    next_greater_lst = [-1] * n
    for i, num in enumerate(nums2):
        ind_dict[num] = i

    for i in range(n):
        for j in range(i + 1, n):
            if nums2[j] > nums2[i]:
                next_greater_lst[i] = nums2[j]
                break
    for num in nums1:
        ans.append(next_greater_lst[ind_dict[num]])
    return ans

def nextGreaterElement_optimized(nums1: list[int], nums2: list[int]) -> list[int]:
    n = len(nums2)
    ind_dict = {} # element : index
    ans = []
    greater_stack = []
    next_greater_lst = [-1] * n

    
    for i, num in enumerate(nums2):
        ind_dict[num] = i
    #nums1 = [1,3,5,2,4], nums2 = [2,4,6,2,3,5]
    greater_stack.append(nums2[-1])
    for i in range(n - 2, -1, -1):
        while len(greater_stack) > 0 and nums2[i] >= greater_stack[-1]:
            greater_stack.pop()
        if len(greater_stack) == 0:
            next_greater_lst[i] = -1
            greater_stack.append(nums2[i])
        else:
            next_greater_lst[i] = greater_stack[-1]
            greater_stack.append(nums2[i])



    for num in nums1:
        ans.append(next_greater_lst[ind_dict[num]])
    #print(ans)
    return ans


def nextGreaterElement_ultra_optimized(nums1: list[int], nums2: list[int]) -> list[int]:
    def next_greater(nums):
        result = [-1] * len(nums)
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ind = stack.pop()
                result[ind] = nums[i]
            
            stack.append(i)
        return result
    next_greater_lst = next_greater(nums2)
    print(next_greater_lst)
    dct = {}
    for i, num in enumerate(nums2):
        dct[num] = i
    
    ans = []
    for num in nums1:
        ans.append(next_greater_lst[dct[num]])
        
    return ans


def nextGreaterElement_ultra_optimized_refactoring(nums1: list[int], nums2: list[int]) -> list[int]:

    def find_next_greater_element_list(nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for current_index, current_element in enumerate(nums):
            while stack and current_element > nums[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = current_element
            stack.append(current_index)
            
        return result
    
    next_greater_element_list = find_next_greater_element_list(nums2)
    element_index_map = {num : index for index, num in enumerate(nums2)}
    answer = [next_greater_element_list[element_index_map[num]] for num in nums1]

    return answer
print(nextGreaterElement_ultra_optimized_refactoring(nums1 = [4,1,2], nums2 = [1,3,4,2]))
