# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        result = [[-1 for _ in range(n)] for _ in range(m)]

        i = j = 0
        direction = 0
        directions_list = [(0, 1), (1, 0), (0, -1), (-1, 0)] # E S W N

        while head:
            result[i][j] = head.val

            test_i = i + directions_list[direction][0]
            test_j = j + directions_list[direction][1]
            # Check if the new direction coordinates are valid, if not change direction
            if (test_i < 0 or test_j < 0) or (test_i >= m or test_j >= n) or (result[test_i][test_j] != -1):
                direction = (direction + 1) % 4
            
            head = head.next
            i += directions_list[direction][0]
            j += directions_list[direction][1]
        
        return result
head = ListNode(0, ListNode(1, ListNode(2, None)))
sol_obj = Solution()
print(sol_obj.spiralMatrix(1, 4, head))