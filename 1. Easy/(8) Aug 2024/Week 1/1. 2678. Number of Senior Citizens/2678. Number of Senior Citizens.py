class Solution:
    def countSeniors(self, details: list[str]) -> int:
        ans = 0
        for citizen in details:
            if int(citizen[11:13]) > 60:
                ans += 1
        return ans