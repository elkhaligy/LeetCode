class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        dollars_obtained = 0
        bills_taken = {
            5 : 0,
            10 : 0,
            20: 0
        }
        for bill in bills:
            bills_taken[bill] += 1
            change = bill - 5
            
            if change == 0:
                continue
            elif change == 5:
                if bills_taken[5] > 0:
                    bills_taken[5] -= 1
                else:
                    return False
            elif change == 10:
                if bills_taken[10] > 0:
                    bills_taken[10] -= 1
                elif bills_taken[5] >= 2:
                    bills_taken[5] -= 2
                else:
                    return False
            elif change == 15:
                if bills_taken[10] > 0 and bills_taken[5] > 0:
                    bills_taken[10] -= 1
                    bills_taken[5] -= 1
                elif bills_taken[5] >= 3:
                    bills_taken[5] -= 3
                else:
                    return False
        
        return True