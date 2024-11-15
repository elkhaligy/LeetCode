def findLengthOfShortestSubarray_TwoPointers(arr: list[int]) -> int:
    left = 0
    right = len(arr) - 1

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    ans = right
    while (left < right) and (left == 0 or arr[left - 1] <= arr[left]):
        
        while right < len(arr) and arr[left] > arr[right]:
            right += 1
        
        ans = min(ans, right - left - 1)
        left += 1

    #print(arr, len(arr), right, ans)
    
    return ans

def findLengthOfShortestSubarray(arr: list[int]) -> int:
    leftSubarray = []
    rightSubarray = []
    prevNum = arr[0]
    n = len(arr)

    leftSubarray.append(prevNum)
    for num in arr[1:]:
        if num >= prevNum:
            leftSubarray.append(num)
            prevNum = num
        else:
            break
            
    prevNum = arr[-1]
    rightSubarray.append(prevNum)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] <= prevNum:
            rightSubarray.append(arr[i])
            prevNum = arr[i]
        else:
            break

    rightSubarray = rightSubarray[::-1]
    leftLen = len(leftSubarray)
    rightLen = len(rightSubarray)
    removedElements = 0
    removedElements = n - (leftLen + rightLen)

    min_removed = min(rightLen, leftLen)
    for i in range(leftLen):
        current_removed = leftLen - (i + 1)
        for j in range(rightLen):
            if rightSubarray[j] < leftSubarray[i]:
                current_removed += 1
            else:
                break
        min_removed = min(min_removed, current_removed)
    
    print(leftSubarray, rightSubarray, len(arr), removedElements, min_removed)
    return min_removed + removedElements
print(findLengthOfShortestSubarray_TwoPointers(arr = [1,2,3,10,4,2,3,5]))
