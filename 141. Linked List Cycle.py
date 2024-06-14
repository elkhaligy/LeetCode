# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()

        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        
        return False
    def hasCycle_sol2(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False