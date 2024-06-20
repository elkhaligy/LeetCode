from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    queue1 = deque([p])
    queue2 = deque([q])
    while queue1 and queue2:
        current_node1 = queue1.popleft()
        current_node2 = queue2.popleft()
        if current_node1 == None and current_node2 != None:
            return False
        if current_node1 != None and current_node2 == None:
            return False
        if current_node1 == None and current_node2 == None:
            return True
        if current_node1.val != current_node2.val:
            return False
        
        if current_node1.left:
            queue1.append(current_node1.left)
        else:
            queue1.append(None)
        if current_node1.right:
            queue1.append(current_node1.right)
        else:
            queue1.append(None)

        if current_node2.left:
            queue2.append(current_node2.left)
        else:
            queue2.append(None)

        if current_node2.right:
            queue2.append(current_node2.right)
        else:
            queue2.append(None)
    return True
    pass



ch2 = TreeNode(8)
ch1 = TreeNode(8)
root1 = TreeNode(5, None, ch2)

ch2 = TreeNode(8)
ch1 = TreeNode(8)
root2 = TreeNode(5, ch1, None)
print(isSameTree(root1, root2))