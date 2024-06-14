class Solution:
    def subset_sum(self, subset, k):
        n = len(subset)
        left = 0
        right = n - 1
        subset.sort()
        a = set()
        for num in subset:
            if num in a:
                return False
            a.add(num + k) 
        # for i in range(n):
        #     for j in range(i + 1,n):
        #         if subset[j] - subset[i] == k:
        #             return False
        return True
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
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
        ans = 0
        #print(result)
        for subset in result:
            if len(subset) == 0:
                continue
            if len(subset) == 1:
                ans += 1
            else:
                if self.subset_sum(subset, k):
                    ans += 1

        return ans
sol_obj = Solution()
#print(sol_obj.beautifulSubsets([4,2,5,9,10,3], 2))

print(sol_obj.subset_sum([4,6], 2))