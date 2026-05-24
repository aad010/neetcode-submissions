# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            else:
                left = dfs(root.left)
                right = dfs(root.right)

                left = [left[0], 1 + left[1]]
                right = [right[0], 1 + right[1]]

                if left[0] and right[0] and abs(right[1] - left[1]) <= 1:
                    return [True, max(left[1], right[1])]
                else:
                    return [False, max(left[1], right[1])]
        
        val = dfs(root)
        return val[0]
