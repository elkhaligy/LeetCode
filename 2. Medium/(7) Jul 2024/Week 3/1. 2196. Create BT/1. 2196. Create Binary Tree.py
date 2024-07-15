# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        nodes_dict = {} # node val: node reference

        # Detect root node
        nodes_set = set()
        for lst in descriptions:
            nodes_set.add(lst[0])
            nodes_set.add(lst[1])
        for lst in descriptions:
            nodes_set.remove(lst[1])

        root_node_val = nodes_set.pop()

        for lst in descriptions:
            node_val = lst[0]
            node_child_val = lst[1]
            left_or_right = lst[2]

            if node_val not in nodes_dict:
                parent_node = TreeNode(node_val)
                nodes_dict[node_val] = parent_node
            else:
                parent_node = nodes_dict[node_val]

            if node_child_val not in nodes_dict:
                child_node = TreeNode(node_child_val)
                nodes_dict[node_child_val] = child_node
            else:
                child_node = nodes_dict[node_child_val]

            if left_or_right == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
        for node_val, reference in nodes_dict.items():
            if node_val == root_node_val:
                return reference

sol_obj = Solution()
print(sol_obj.createBinaryTree(descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))