# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        curr_max = -101
        def dfs(root, curr_max):
            if not root:
                return
            else:
                if root.val >= curr_max:
                    curr_max = root.val
                    res.append(root.val)
                dfs(root.left, curr_max)
                dfs(root.right, curr_max)
                return
        dfs(root, curr_max)
        return len(res)