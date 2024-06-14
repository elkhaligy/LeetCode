from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: TreeNode) -> list[float]:
    queue = deque([root])
    levels = []
    ans = []
    while queue:
        cur_level_len = len(queue)
        cur_level = []

        for _ in range(cur_level_len):
            current_node = queue.popleft()
            cur_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        levels.append(cur_level)
    
    print(levels)
    for lst in levels:
        ans.append(sum(lst) / len(lst) )
    return ans
    pass



ch2 = TreeNode(8)
ch1 = TreeNode(4)
root = TreeNode(5, ch1, ch2)

print(averageOfLevels(root))