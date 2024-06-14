from collections import defaultdict
def maximumSubarraySum(nums: list[int], k: int) -> int:
        window_start = 0
        window_end = 0
        n = len(nums)
        subsets_window = []
        ans = 0
        cur_sum = 0
        cnt = 0
        while window_end < n:             
            if nums[window_end] in subsets_window:
                 #window_end += 1
                cur_sum -= nums[window_start]
                subsets_window[window_start] = -1
                 
                window_start += 1
                cnt = 0
                 #continue
            cnt += 1
            subsets_window.append(nums[window_end])
            cur_sum += nums[window_end]
            if window_end == k - 1 + window_start:
                # if len(subsets_window[window_start:]) == len(set(subsets_window[window_start:])):
                #     #subsets_sum.append(sum(subsets_window)) 
                ans = max(ans, cur_sum)
                cur_sum -= subsets_window[window_start]
                subsets_window[window_start] = -1
                window_start += 1
                cnt = 0
            window_end += 1

        return ans
def maximumSubarraySum_Sol2_90TestCases(nums: list[int], k: int) -> int:
    window_start = 0
    window_end = 0
    n = len(nums)
    ans = 0
    cur_sum = 0
    dct = defaultdict(int)
    while window_end < n:             
        dct[nums[window_end]] += 1
        if dct[nums[window_end]] > 1:
            #dct[nums[window_end]] -= 1
            for key in dct:
                    dct[key] = 0
            dct[nums[window_end]] += 1
            window_start = window_end
            cur_sum = 0

        cur_sum += nums[window_end]

        if window_end == k - 1 + window_start:
            ans = max(ans, cur_sum)
            cur_sum -= nums[window_start]
            dct[nums[window_start]] -= 1
            window_start += 1
    
        window_end += 1

    return ans

def maximumSubarraySum_Sol3(nums: list[int], k: int) -> int:
    """
    Variables:
        start: Start index of the window
        end: End index of the window
        ans: Final answer to be returned
        cur_sum: Sum of the current window
        occu_dct: Occurance dictionary, element: number of occurances
        distinct: A counter that counts number of distinct element in a window
    """
    start = 0
    end = 0
    ans = 0
    cur_sum = 0
    occu_dct = defaultdict(int)
    distinct= 0

    while end < len(nums):
        # Add the current element to cur_sum
        cur_number = nums[end]
        cur_sum += cur_number
        # Register element occurance in the dictionary
        occu_dct[cur_number] += 1
        # If the element occured only 1 time then it is distinct
        if occu_dct[cur_number] == 1:
            distinct += 1

        # If the window width is k then start to operate on this window
        if end == k + start - 1:
            # Debug prints
            print(nums[start:end + 1])
            print(occu_dct)
            print(distinct)
            # Only update answer if the number of distinct elements in this window is k
            if distinct == k:
                ans = max(ans, cur_sum)
            # Subtract first number from the cur_sum to move the window
            first_number = nums[start]    
            cur_sum -= first_number
            
            # Update the occurance dictionary
            # If the first element that we will remove from the window occured less than or equal to 1
                # then remove it from the dictionary and decrease distinct elements by 1
            # If it happened more than 1 then decrease its count by 1 and do not decrease distinct counter
                # because the element is still in the current window after update
            if occu_dct[first_number] <= 1:
                occu_dct.pop(first_number, 0)
                distinct -= 1
            else:
                occu_dct[first_number] -= 1
            
            # Move the start of the window to next element
            start += 1

        end += 1
        
    return ans
         
         

print(maximumSubarraySum_Sol3(nums = [1,1,1,7,8,8], k = 3))


