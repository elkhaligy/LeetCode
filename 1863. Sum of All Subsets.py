def subsetXORSum(nums: list[int]) -> int:
    res = []
    cur = []
    def backtrack(index):
        if index == len(nums):
            res.append(cur[:])
            return

        backtrack(index + 1)
        cur.append(nums[index])
        backtrack(index + 1)
        cur.pop()
    backtrack(0)
    print(res)


print(subsetXORSum([1,2,3]))