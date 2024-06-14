# https://leetcode.com/problems/permutations/description/
import itertools
def permute(nums: list[int]) -> list[list[int]]:
        def permute_rec(cur_perm):
            if len(cur_perm) == len(nums):
                ans.append(cur_perm[:])
                return

            for num in nums:
                if num in cur_perm:
                    continue
                cur_perm.append(num)
                permute_rec(cur_perm)
                cur_perm.pop()
        cur_perm = []
        ans = []
        permute_rec(cur_perm)
        return ans


print(permute([1,2,3]))