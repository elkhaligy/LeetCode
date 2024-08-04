from collections import defaultdict
class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        my_dct =  [defaultdict(int) for _ in range(n)]
        for player in pick:
            my_dct[player[0]][player[1]] += 1
        
       # print(my_dct)
        ans = 0

        for i in range(n):
                player_wins = False
                for count in my_dct[i].values():
                    if count > i:
                        player_wins = True
                        break
                if player_wins:
                    ans += 1
    
        return ans