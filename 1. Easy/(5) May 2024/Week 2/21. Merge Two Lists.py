# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ans = ListNode()
        cur = ans
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next= list2
                list2 = list2.next
            
            cur = cur.next

        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        cur.next = None

        return ans.next

# ll 1
node3 = ListNode(4)
node2 = ListNode(2, node3)
ll1_head = ListNode(1, node2)

# ll 2
node3 = ListNode(4)
node2 = ListNode(3, node3)
ll2_head = ListNode(1, node2)
        
sol_obj = Solution()
lst = sol_obj.mergeTwoLists(ll1_head, ll2_head)
while lst != None:
    print(lst.val)
    lst = lst.next


print(ll1_head.next.val)