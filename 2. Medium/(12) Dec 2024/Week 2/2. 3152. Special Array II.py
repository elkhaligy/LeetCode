def isArraySpecial_TLE(nums: list[int], queries: list[list[int]]) -> list[bool]:
    def isArraySpecial(nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        prevNum = nums[0]
        for num in nums[1:]:
            if num & 1 == prevNum & 1:
                return False
            prevNum = num
            
        return True
    answers = []
    for query in queries:
        answers.append(isArraySpecial(nums[query[0]:query[1] + 1]))


    return answers 

def isArraySpecial(nums: list[int], queries: list[list[int]]) -> list[bool]:
    n = len(nums)
    start = end = 0
    nextIndexList = []
    answer = []

    while start < n:
        end = max(end, start)

        while end < n - 1 and nums[end] & 1 != nums[end + 1] & 1:
            end += 1


        nextIndexList.append(end)
        start += 1
    #print(nextIndexList)
    for query in queries:
        answer.append(nextIndexList[query[0]] >= query[1])
    
    return answer
print(isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))
