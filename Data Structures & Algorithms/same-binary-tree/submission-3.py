# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(rootOne, rootTwo):
            if not rootOne and not rootTwo:
                return True
            elif not rootOne and rootTwo:
                return False
            elif rootOne and not rootTwo:
                return False
            else:
                if rootOne.val == rootTwo.val:
                    return True and dfs(rootOne.left, rootTwo.left) and dfs(rootOne.right, rootTwo.right)
                else:
                    return False

        return dfs(p, q)