# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_addresses_dct = {}

        dummy_A = headA
        while dummy_A:
            nodes_addresses_dct[dummy_A] = dummy_A.val
            dummy_A = dummy_A.next
        
        dummy_B = headB
        while dummy_B:
            if dummy_B in nodes_addresses_dct:
                return dummy_B
            dummy_B = dummy_B.next

        return None

# O(1) Space Solution
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = 0
        len_B = 0
        dummy_A = headA
        while dummy_A:
            len_A += 1
            dummy_A = dummy_A.next
        
        dummy_B = headB
        while dummy_B:
            len_B += 1
            dummy_B = dummy_B.next

        dummy_A = headA
        dummy_B = headB
        if len_A > len_B:
            diff = len_A - len_B
            for _ in range(diff):
                dummy_A = dummy_A.next
            
            while dummy_A and dummy_B:
                if dummy_A == dummy_B:
                    return dummy_A
                dummy_A = dummy_A.next
                dummy_B = dummy_B.next
            return None
        else:
            diff = len_B - len_A
            for _ in range(diff):
                dummy_B = dummy_B.next
            
            while dummy_A and dummy_B:
                if dummy_A == dummy_B:
                    return dummy_A
                dummy_A = dummy_A.next
                dummy_B = dummy_B.next
            
            return None




# intersected nodes
node_i_3 = ListNode(5)
node_i_2 = ListNode(4, node_i_3)
node_i_1 = ListNode(8, node_i_2)

# ll A
node_a_2 = ListNode(1, node_i_1)
node_a_1 = ListNode(4, node_a_2)

# ll B
node_b_3 = ListNode(1, node_i_1)
node_b_2 = ListNode(6, node_b_3)
node_b_1 = ListNode(5, node_b_2)

sol_obj = Solution2()
ans_node = sol_obj.getIntersectionNode(node_a_1, node_b_1)

print(ans_node.val)