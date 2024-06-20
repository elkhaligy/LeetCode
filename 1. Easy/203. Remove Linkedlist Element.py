class LinkedList:
    head = None
    def append(self, a):
        node = ListNode(a)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.next = None

    def print(self):
        a = self.head
        while a:
            print(a.val, end=' ')
            a = a.next
        print()
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = head
        cur = head.next
        # check first node


        # while cur:
        #     if cur.val == val:
        #         prev.next = cur.next
        #     cur = cur.next
        #     prev = prev.next
        
        while cur:
            if prev.val == val:
                head = head.next
                prev = prev.next
                cur = cur.next
            elif cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        
        if head.val == val:
            head = None
        return head
    # best sol
    def removeElements_Sol2(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head

        current_node.next.next.val = 6


        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        
        return dummy_head.next

ll = LinkedList()

ll.append(7)
ll.append(7)
ll.append(7)
ll.append(7)
ll.append(7)

ll.print()
head = ll.head

sol_obj = Solution()
new_head = sol_obj.removeElements_Sol2(head, 7)

while new_head:
    print(new_head.val, end=' ')
    new_head = new_head.next