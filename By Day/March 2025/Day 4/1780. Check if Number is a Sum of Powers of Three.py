class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 10 ^ 7 -> 10_000_000
        # 3 ^ x = 10_000_000
        # x ~= 15 
        
        # I want a function that multiply three by three until we reach the number given to it or exceeds it

        # We can inlcude the 3 ^ x thus reducing target -> n - 3 ^ x
        # or we can skip and go on with the power

        # ex -> 9
        # 3 ^ 0 take it -> 8
        # 3 ^ 1 take it -> 5
        # 3 ^ 2 take it -> -1 Nope return false

        def checkPowers(currPower, currNum):
            if currNum == 0:
                return True
            if (3 ** currPower > currNum):
                return False

            option1 = checkPowers(currPower + 1, currNum - 3 ** currPower)
            option2 = checkPowers(currPower + 1, currNum)
            return option1 or option2
        
        return checkPowers(0, n)