# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return
        dummy = head
        prev = head
        head = head.next
        while head:
            if prev.val == head.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        
        return dummy

# 1 1 2 3 3


node5 = ListNode(3)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)

sol_obj = Solution()
ans = sol_obj.deleteDuplicates(node1)

while node1:
    print(node1.val, end='')
    node1 = node1.next
