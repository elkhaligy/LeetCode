# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root is None:
            return False
        
        return self.check(head, root)
    
    def check(self, head, root):
        if self.dfs(head, root):
            return True
        
        return self.check(head, root.left) or self.check(head, root.right)

    def dfs(self, head, root):
        if head is None:
            return True
        if root is None:
            return False
        if root.val != head.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)