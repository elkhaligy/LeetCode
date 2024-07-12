from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return root
        queue = deque([root])
        ans = []
        while queue:
            level_len = len(queue)

            for _ in range(level_len):
                cur_node = queue.popleft()

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            ans.append(cur_node.val)
        return ans