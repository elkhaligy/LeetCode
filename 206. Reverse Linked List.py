# Definition for singly-linked list.
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
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = head
        stack = []
        while dummy:
            stack.append(dummy.val)
            dummy = dummy.next
        
        #print(f"stack: {stack}")

        ll = LinkedList()
        for i in range(len(stack) - 1, -1, -1):
            ll.append(stack[i])
        
        return ll.head
    
    def reverseList_Sol2(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        nxt = cur.next

        while nxt:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next
        cur.next = prev
        return cur

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()
head = ll.head

sol_obj = Solution()
new_head = sol_obj.reverseList_Sol2(head)

while new_head:
    print(new_head.val, end= ' ')
    new_head = new_head.next