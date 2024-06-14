# class Solution:
#     def rob(self, nums: list[int]) -> int:
        


# sol_object = Solution()
# print(sol_object.rob([1,2,3,1]))
houses = [2,7,9,3,1]
result = []
def rec(index, path, s):
    
    if index >= len(houses):
        if path:
            result.append(path[:])
        return sum(path)
    print(houses[index])
    s += houses[index]
    sum1 = rec(index + 1, path, s)
    path.append(houses[index])
    sum2 = rec(index + 2, path, s)
    path.pop()
    return max(sum1, sum2)

print(rec(0, [], 0))
print(result)

# Recursion is frames, each frame is related to the frame it called, by variables passed
# photo 1