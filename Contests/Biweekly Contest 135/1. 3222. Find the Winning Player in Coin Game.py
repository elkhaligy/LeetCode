class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        cur_turn = 0
        while x >= 1 and y >= 4:
            cur_turn ^= 1
            x -= 1
            y -= 4
            
        
        return "Bob" if cur_turn == 0 else "Alice"