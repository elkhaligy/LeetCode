class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        result = []
        current = []
        def fn(i):
            if i == len(nums):
                result.append(current[:])
                return
            
            fn(i + 1)

            current.append(nums[i])
            fn(i + 1)
            current.pop()
        
        fn(0)
        return result
sol_obj = Solution()
print(sol_obj.subsets([4,2,5,9,10,3]))