class Solution():
    def search(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def oleh(nums: list[int], l, r):
            if l > r:
                return -1
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid
            # [4,5,6,7,0,1,2]
            # if left half is sorted
            if nums[mid] >= nums[l]:
                if target <= nums[mid] and target >= nums[l]:
                    return oleh(nums, l, mid)
                else:
                    return oleh(nums, mid + 1, r)
            # if right half is sorted
            else:
                if target <= nums[r] and target >= nums[mid]:
                    return oleh(nums, mid, r)
                else:
                    return oleh(nums, l, mid - 1)
        ans = oleh(nums, 0, len(nums) - 1)
        return ans

ob = Solution()
print(ob.search([4,5,6,7,0,1,2], 3))
        