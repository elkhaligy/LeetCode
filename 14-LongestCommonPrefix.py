class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        chrInd = 0
        
        ans = True
        myLen = float('inf')
        for s in strs:
            myLen = min(myLen, len(s))

        for i in range(myLen):
            myChr = strs[0][chrInd]
            for j in range(1, len(strs)):
                ans &= (myChr == strs[j][chrInd])
            if ans:
                chrInd += 1
        return strs[0][:chrInd]
                    

obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])