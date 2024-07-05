# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        prev = head
        curr = head.next
        nxt = curr.next

        if head == None or nxt == None:
            return [-1, -1]
        
        indices_list = []
        curr_pos = 1
        while nxt:
            if prev.val < curr.val > nxt.val:
                indices_list.append(curr_pos)
            elif prev.val > curr.val < nxt.val:
                indices_list.append(curr_pos)
            
            prev = curr
            curr = nxt
            nxt = nxt.next
            curr_pos += 1
        #print(indices_list)
        if len(indices_list) <= 1:
            return [-1, -1]
        else:
            min_dst = float('inf')
            prev = indices_list[0]
            
            for num in indices_list[1:]:
                curr_min = num - prev
                min_dst = min(min_dst, curr_min)
                prev = num
            return [min_dst, indices_list[-1] - indices_list[0]]
