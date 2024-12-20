from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode) -> TreeNode:

        # BFS
        queue = deque([root])
        currLevel = 0
        while queue:
            nodesVal = []
            nodes = []
            for _ in range(len(queue)):
                currNode = queue.popleft()
                if currLevel % 2 == 1:
                    nodesVal.append(currNode.val)
                    nodes.append(currNode)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            currLevel += 1
            if len(nodesVal) > 0:
                nodesVal = nodesVal[::-1]
                for i in range(len(nodes)):
                    nodes[i].val = nodesVal[i]
        
        return root