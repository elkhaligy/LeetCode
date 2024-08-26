
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        traversal_lst = []

        def helper(root):
            if root == None:
                return
            for child in root.children:
                helper(child)

            traversal_lst.append(root.val)
        
        helper(root)
        return traversal_lst