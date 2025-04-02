class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        # Recurrence relation: dp[i] = max(question[i][0] + dp[i + question[i][1] + 1], dp[i + 1])
        # dp[i] represent the max points that can be obtained from question i onward

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            nextIndex = i + questions[i][1] + 1
            if nextIndex < n:
                dp[i] = max(points + dp[nextIndex], dp[i + 1])
            else:
                if i + 1 < n:
                    dp[i] = max(points + 0, dp[i + 1])
                else:
                    dp[i] = points
            
        return dp[0]




solObj = Solution()
print(solObj.mostPoints([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]))