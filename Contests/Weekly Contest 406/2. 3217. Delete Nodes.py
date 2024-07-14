class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(nums: list[int], head: ListNode) -> ListNode:
        to_be_deleted = set(nums)
        new_ll = []
        dummy = head

        while dummy:
            if not (dummy.val in to_be_deleted):
                new_ll.append(dummy.val)
            dummy = dummy.next
        