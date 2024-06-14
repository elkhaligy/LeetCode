# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1206044060/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if(prices[l]>prices[r]):
                l = r
            maxProfit = max(maxProfit,prices[r]-prices[l])
            r = r+1
        return maxProfit
obj = Solution()
obj.maxProfit([7,1,5,3,6,4])