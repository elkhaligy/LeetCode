import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        curr = head.next
        prev = head

        while curr:
            gcd_val = math.gcd(curr.val, prev.val)
            new_node = ListNode(gcd_val, curr)
            prev.next = new_node

            curr = curr.next
            prev = prev.next.next

        return head    


