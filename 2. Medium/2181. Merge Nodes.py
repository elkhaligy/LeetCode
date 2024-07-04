# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        if not self.head:
            self.head = ListNode(value, None)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value, None)
    def from_list(self, lst):
        for value in lst:
            self.append(value)

class Solution:
    def mergeNodes_TLE(self, head: ListNode) -> ListNode:
        original_values = []
        dummy = head
        while dummy:
            original_values.append(dummy.val)
            dummy = dummy.next
        
        current_count = 0
        zero_count = 0
        modified_values = []
        for num in original_values:
            current_count += num

            if num == 0:
                zero_count += 1
            if zero_count == 2:
                modified_values.append(current_count)
                current_count = 0
                zero_count -= 1
        
        new_ll = LinkedList()
        new_ll.from_list(modified_values)
        return new_ll.head
    
    def mergeNodes_ac(self, head: ListNode) -> ListNode:
        modifier_pntr = head
        traversal_pntr = head.next
        current_count = 0

        while traversal_pntr.next:
            current_count += traversal_pntr.val

            if traversal_pntr.val == 0:
                modifier_pntr.val = current_count
                modifier_pntr = modifier_pntr.next
                current_count = 0
            
            traversal_pntr = traversal_pntr.next

        modifier_pntr.val = current_count
        modifier_pntr.next = None

        return head