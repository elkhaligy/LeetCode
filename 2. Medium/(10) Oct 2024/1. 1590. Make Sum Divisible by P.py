class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        # We need sum % p = 0
        # sum % p != 0 so sum % p = x
        # we need to remove the subarray that has sum equal to x
        # arr       :  [3, 1, 4, 2]
        # sum of arr = 10
        # x = 10 % 6 = 4
        # if we find a subarray that has total sum of 4 and remove it, the rest of the elemment's sum will be divisible by p
        # Prefix sum: [0, 3, 4, 8, 10]
        # (s2 - s1) % p = x
        # so if the above equation is true the answer is just the s2 - s1
        # but I need to make things faster, instead of brute forcing all sums with each others
        # lets manipulate the equation
        # s1 = (s2 - x) % p
    
        n = len(nums)
        x = sum(nums) % p

        # If x is already 0 then no need to remove any elements
        if x == 0:
            return 0 

        prefix_sums = [0]
        for i in range(n):
            prefix_sums.append(prefix_sums[i] + nums[i])

        pos_dict = {0 : -1}
        answer = n
        for i, p_sum in enumerate(prefix_sums[1:]):
            s2 = p_sum % p
            s1 = (s2 - x + p) % p

            if s1 in pos_dict:
                answer = min(answer, i - pos_dict[s1])
            
            pos_dict[s2] = i
        
        return answer if answer != n else -1
